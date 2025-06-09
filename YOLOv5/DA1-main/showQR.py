
from PIL import ImageDraw
from PIL import Image, ImageFont

image = Image.open('QR.png')
width, height = image.size
draw = ImageDraw.Draw(image)
text_cinema = "RPG Cinema"
text_seat = "Seat: 15C Balcony"
font = ImageFont.load_default()
draw.text((40, 5), text_cinema, font=font)
draw.text((40,height - 20), text_seat, font=font)
image.save("QRnew.png")
