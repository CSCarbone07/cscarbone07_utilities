import qrcode
import os

currentPath = os.path.dirname(os.path.abspath(__file__))
outputPath = currentPath + "/tmp"
outputName = "/"
outputFormat = ".png"

print(outputPath)


qr_text = 1



for i in range(0,26):
    file_out = outputPath + outputName + str(i) + outputFormat
    qr_text = str(i)
    qr = qrcode.QRCode(
            version=1,
            box_size=25,
            border=5)
    qr.add_data(qr_text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_out)
