import cv2

#img = cv2.imread("img.png")
#median = cv2.m(img, 5)
#cv2.imwrite("img_m.png", median)

#print(median)
from PIL import Image, ImageFilter

# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
#image = Image.open(r"La")

# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
im = Image.open("img.png")

#rotate image
angle = 25
out = im.rotate(angle)
out.save('img_rate.png')
image = out
image.show()