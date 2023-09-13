import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

# color in "make_image" may be as (back_color=(255, 195, 235), fill_color=(55, 95, 35))
img = qr.make_image(fill_color="black", back_color="white")

img.save("welcome.png")
