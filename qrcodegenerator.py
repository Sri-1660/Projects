import qrcode
import image
qr = qrcode.QRCode(
    version =15,
    box_size=10,
    border = 5
)

data ="https://www.youtube.com/watch?v=8XhGC9VxNu0&t=13s"
qr.add_data(data)
qr.make(fit= True)
img= qr.make_image(fill="black",back_color= "white")
img.save("test.png")