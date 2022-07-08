import qrcode
img = qrcode.make('https://www.youtube.com/channel/UCZxY1hoDNOAgcxu6ZiAiddA')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/channel/UCZxY1hoDNOAgcxu6ZiAiddA')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")