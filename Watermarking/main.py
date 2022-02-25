#TODO
#Create a gui that lets you select a picture, where you want to put the watermark, what text, what color it should be
#and where to save it


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def watermark(img, w_text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./arial.ttf", 32)
    draw.text((0, 0), w_text, (0, 0, 0), font=font)
    img.save('watermarked.jpg')


image_source = Image.open("img.jpg")
watermark_text = "TEST"
watermark(image_source, watermark_text)