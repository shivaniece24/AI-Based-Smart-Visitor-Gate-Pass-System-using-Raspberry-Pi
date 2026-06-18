import qrcode

def generate_qr(data, filename):

    qr = qrcode.QRCode(

        version=1,

        box_size=10,

        border=5

    )

    qr.add_data(data)

    qr.make(fit=True)

    image = qr.make_image()

    image.save(filename)

    return filename
