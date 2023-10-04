import requests

image = requests.get('url картинки')
with open('файл', 'wb') as f:  # формат файла сохранить как у картинки
    f.write(image.content)
