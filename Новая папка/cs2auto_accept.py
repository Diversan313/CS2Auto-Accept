import cv2
import numpy as np
import pyautogui
import time
import mss
import os

# Настройки
ACCEPT_FOLDER = "accepts"
MATCH_FOLDER = "in_match"

ACCEPT_THRESHOLD = 0.4
MATCH_THRESHOLD = 0.55

CHECK_INTERVAL = 2       # интервал между проверками
MATCH_SLEEP = 40         # интервал проверки, если ты в матче

def screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screen = np.array(sct.grab(monitor))
        return cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)

def load_templates(folder):
    templates = []
    for file in os.listdir(folder):
        if file.endswith(".png"):
            path = os.path.join(folder, file)
            img = cv2.imread(path)
            if img is not None:
                templates.append((img, file))
    return templates

def match_templates(screen, templates, threshold):
    for template, name in templates:
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            h, w, _ = template.shape
            center = (max_loc[0] + w // 2, max_loc[1] + h // 2)
            return center, name, max_val
    return None, None, 0.0

def wait_until_disappears(templates, threshold, max_wait=10):
    start = time.time()
    while time.time() - start < max_wait:
        screen = screenshot()
        coords, _, _ = match_templates(screen, templates, threshold)
        if not coords:
            return True
        time.sleep(0.5)
    return False

def main():
    accept_templates = load_templates(ACCEPT_FOLDER)
    match_templates_set = load_templates(MATCH_FOLDER)

    if not accept_templates:
        print("❌ Нет шаблонов accept в папке.")
        return

    while True:
        screen = screenshot()

        # Проверка на кнопку "Принять"
        coords, name, confidence = match_templates(screen, accept_templates, ACCEPT_THRESHOLD)
        if coords:
            print(f"🎯 Найдена кнопка [{name}] (совпадение {confidence:.3f}) — нажимаю")
            pyautogui.moveTo(coords[0], coords[1], duration=0.2)
            pyautogui.click()
            wait_until_disappears(accept_templates, ACCEPT_THRESHOLD)
            continue

        # Проверка: в матче ли ты?
        in_match = False
        if match_templates_set:
            match_coords, match_name, match_conf = match_templates(screen, match_templates_set, MATCH_THRESHOLD)
            if match_coords:
                print(f"🎮 В матче — найдено [{match_name}] (совпадение {match_conf:.3f})")
                in_match = True

        if in_match:
            while True:
                time.sleep(MATCH_SLEEP)
                screen = screenshot()
                match_coords, _, _ = match_templates(screen, match_templates_set, MATCH_THRESHOLD)
                if not match_coords:
                    break
        else:
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
