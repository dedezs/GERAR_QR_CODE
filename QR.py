import pyqrcode
import png

link = "https://www.antlia.com.br/"
qr_code = pyqrcode.create(link)
qr_code.png("antlia.png", scale=5)