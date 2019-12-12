import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!
# Median pixel filter, taken from https://note.nkmk.me/en/python-opencv-pillow-image-size
from PIL import Image

for i in range(width):
    for j in range(height):
        R, G, B = img.getpixel((i, j))

        if R > 0:
            R += 0
        if G > 0:
            G += 50
        if B > 0:
            B += 80

        new_img.putpixel((i, j), (R, G, B))

new_img.save(output_path)