# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].
# print(data)
# For example:
# for row in data:
#   print(' '.join('{:3}'.format(value) for value in row))

# Here's another more compact representation.
# chars = '@%#*+=-:. '  # Change as desired.
# scale = (len(chars)-1)/255.
# print()
# for row in data:
#   print(' '.join(chars[int(value*scale)] for value in row))
import numpy as np
from PIL import Image

from read_text import get_watermark
from random import randint

img = Image.open('img.png').convert('L')  # convert image to 8-bit grayscale
WIDTH, HEIGHT = img.size

data = list(img.getdata())  # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]

watermark = get_watermark()


class Dim:
    def __init__(self, value, row, col, frequency, diff=0):
        self.value = value
        self.row = row
        self.col = col
        self.frequency = frequency
        self.diff = diff

    def to_string(self):
        return "{value:" + str(self.value) + ", row:" + str(self.row) + ", col:" + str(self.col) + ", frequency:" + str(
            self.frequency) + ", diff:" + str(self.diff) + "}"


def watermarked(image_array, watermark_list):
    list_dim = list()
    for value in watermark_list:
        dim_frequency = 0
        dim_row = 0
        dim_col = 0
        dim_diff = 0
        found = False
        for dim in list_dim:
            if dim.value == value:
                found = True
                dim_row = dim.row
                dim_col = dim.col
                dim_diff = dim.diff
                dim_frequency = dim.frequency
        if found:
            list_dim.append(Dim(value, dim_row, dim_col, dim_frequency, dim_diff))
        else:
            found_in_image = False
            for row in range(WIDTH):
                for col in range(HEIGHT):
                    if value == image_array[row][col]:
                        dim_frequency += 1
                        dim_row = row
                        dim_col = col
                        found_in_image = True
            if found_in_image:
                list_dim.append(Dim(value, dim_row, dim_col, dim_frequency))
            else:
                dim_row = randint(0, WIDTH)
                dim_col = randint(0, HEIGHT)
                dim_diff = data[row][col] - value
                list_dim.append(Dim(value, dim_row, dim_col, 1, dim_diff))
    return list_dim


def extract_watermark(image_array, watermark_table):
    watermark = [chr(image_array[wtr.row][wtr.col]) for wtr in watermark_table]
    print(''.join(watermark))


watermark_table = watermarked(data, watermark)
[print(dim.to_string()) for dim in watermark_table]
extract_watermark(data, watermark_table)
