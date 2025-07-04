# **Use for researching and testing, stable version is active**

## CS2Auto-Accept

CS2Auto-Accept — это скрипт для автоматического принятия матчей в игре Counter-Strike 2 с помощью компьютерного зрения.

Скрипт анализирует экран, используя шаблоны изображений кнопки "Принять" и индикаторов нахождения в матче. Если кнопка обнаружена, программа автоматически нажимает на неё. Если определяется, что игрок уже находится в матче, скрипт временно приостанавливает свои действия.

### Возможности

- Автоматический поиск и нажатие кнопки "Принять" на экране.
- Определение статуса "в матче" с помощью шаблонов.
- Гибкая настройка порогов срабатывания и интервалов проверки.
- Использование шаблонов изображений (PNG) для обнаружения нужных элементов интерфейса игры.

### Требования

- Python 3.7+
- Необходимые библиотеки: `opencv-python`, `numpy`, `pyautogui`, `mss`

Установка зависимостей:
```bash
pip install opencv-python numpy pyautogui mss
```

### Использование

1. Поместите шаблоны кнопки "Принять" в папку `accepts`, а шаблоны для определения статуса "в матче" — в папку `in_match`.
2. Запустите скрипт:
```bash
python CS2-at-ac/cs2auto_accept.py
```
3. Скрипт начнет автоматически мониторить экран и принимать матчи.



- Используйте на свой страх и риск. Проект создан для исследовательских и тестовых целей.
- Не предназначено для использования в мультиаккаунтинге или нарушении правил игры.

## Автор

[https://github.com/Diversan313](https://github.com/Diversan313)
