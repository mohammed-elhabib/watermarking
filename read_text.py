from PIL import Image


def get_watermark():
    text = input("enter a string to convert into ascii values:")
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    return ascii_values
def get_watermark_imge():
    img = Image.open("Webp.net-resizeimage (1).png").convert('L')
    WIDTH, HEIGHT = img.size
    return  list(img.getdata()),WIDTH,HEIGHT