import pyautogui

# установка пакета из кода
# import pip
# pip.main(['install', 'pyautogui'])
# pip.main(['uninstall','pyautogui'])

# проверка установлен ли пакет
# import sys
# if 'pyautogui' in sys.modules:
#     print(1)


for i in range(25):
    pyautogui.keyDown('capslock')
    pyautogui.keyUp('capslock')
    pyautogui.keyDown('numlock')
    pyautogui.keyUp('numlock')
    pyautogui.keyDown('scrolllock')
    pyautogui.keyUp('scrolllock')
