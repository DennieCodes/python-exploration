# convert jpg files in a directory into a png files

import sys
import os #paths
from PIL import Image

# use the sys to grab the first and second argument

# go to a directory - do some logic - output another directory

image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the entire pokedex folder and then
# convert images to png

for filename in os.listdir(image_folder):
    # print(filename)
    img = Image.open(f'{image_folder}/{filename}')
    # print(img)
    cleanup_name = os.path.splitext(filename)[0] # splits the filename and its exptension
    print(cleanup_name)
    img.save(f'{output_folder}/{cleanup_name}.png', 'png')

    # python jpg_to_png.py ./pokedex ./New