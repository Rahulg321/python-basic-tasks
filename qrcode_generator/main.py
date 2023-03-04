#convert a text or a link to a qr code using python
#install the libraries
#recieve a text and generate a qr code
#save the qr code as a image

import qrcode

def generate_qrcode(text = None):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('myqr.png')
    

def main():
    generate_qrcode("https://www.google.com")

main()

