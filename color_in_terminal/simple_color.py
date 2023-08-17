from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

# цвет текста:
print(Fore.BLUE + 'Текст синего цвета')
print(Fore.LIGHTBLUE_EX + 'Текст светлосинего цвета')
print(Fore.LIGHTGREEN_EX + 'Текст светлозеленого цвета')
print(Fore.MAGENTA + 'Цвет маджента (фиолетовый кажись)')
# цвет фона
print(Back.WHITE + 'Фон текста')
print(Back.MAGENTA + 'Фон текста')
print(Back.LIGHTGREEN_EX + 'Фон текста')
# совмещение и фона и текста
print(Back.BLACK + Fore.LIGHTGREEN_EX + 'Фон текста')
# стили
print(Style.BRIGHT + 'типа жирный')
print(Style.NORMAL + 'обычный')

# совмещение и фона и текста и стиля
print(Back.BLACK + Fore.LIGHTGREEN_EX + Style.BRIGHT + ' Какой-то текст ')

# сброс всего
print(Style.RESET_ALL)
print('Вернулись в исходное')
