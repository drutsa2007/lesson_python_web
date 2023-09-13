import segno
from segno import helpers

qrcode = segno.make('http://yandex.ru')
# Dark modules with alpha transparency #xxxxxx00
qrcode.save('welcome.png', scale=5, border=15, dark='#0000ffff', light='lightblue')
# qrcode.save('welcome.pdf', scale=10)  # можно в pdf
# qrcode.save('welcome.svg')  # можно в svg

qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')
qrcode.save('wifi-access.png', scale=10)

qrcode = helpers.make_mecard(name='Shittu Olumide',
                             email=('me@example.com', 'email@example.com'),
                             url=['http://www.example.com', 'https://example.come/~olu'])
qrcode.save('mycontact.png', scale=5)
