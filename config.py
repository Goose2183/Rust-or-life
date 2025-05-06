import os
import sys

def image_path():
    """Получает абсолютный путь к ресурсу, независимо от того, запущен ли скрипт как .exe или .py."""
    if getattr(sys, 'frozen', False):
        # Если приложение запущено как .exe
        base_path = sys._MEIPASS
    else:
        # Если приложение запущено из исходного кода
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, 'resources')


geometry = "600x400"
label_rust = {"text":"Rust","cords":[120,100]}
label_life ={"text":"Личная жизнь", "cords":[120,300]}
btn_rust = {"cords":[91,170]}
btn_life = {"cords":[350,170]}