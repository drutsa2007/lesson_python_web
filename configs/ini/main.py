# импортируем библиотеку
import configparser

# создаём объекта парсера
config = configparser.ConfigParser()
# считываем файл конфигурации
config.read("settings.ini")

# теперь можем обращаться к любому значению
print(config["Block1"]["sekret"])
print(config["Settings_Block2"]["host"])
