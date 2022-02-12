from PIL import Image
import math
from IPython.display import display
import time

# Interpret raw visual data from a text file
# Implementation #1
# Converting data to a readable PNG file format

def read_img(difficulty):
    # Open source text file for reading
    num_file = open("jspragu2_" + difficulty + ".txt","r")
    num_string = num_file.readline()

    # Remove brackets and linebreaks
    num_string = num_string.strip("[]\n")

    # Add numbers to list with the ", " being the split between numbers 
    num_list = num_string.split(", ")

    # Convert each number in list to a float from string
    for i in range(len(num_list)):
        num_list[i] = float(num_list[i])

    # Determine size of image
    # Width is guaranteed 256 for easy and medium, 512 for hard
    if difficulty == "hard":
        width = 512
    else:
        width = 256
    height = int(len(num_list) / width)

    # Create new image file and load its pixels array
    img = Image.new('RGB',(width,height),"white")
    pixels = img.load()

    # Loop through list and find highest value
    max = 0
    for i in range(len(num_list)):
        if num_list[i] > max:
            max = num_list[i]
    # Divide 255 by max to determine factor that the raw numbers should be multiplied by
    max = 255 / max

    # For loop to interpret every number in num_list as a pixel
    for i in range(len(num_list)):
        # Change the RGB value of each pixel of image to intensity found in list
        # x = i%/width (x increases once every loop iterations)
        # y = i/height (y increases once every *size* loop iterations) 
        # RGB values multiplied by factor max and subtracted from 255 to invert colors
        pixels[i%width,i/height] = (int(255-num_list[i]*max),int(255-num_list[i]*max),int(255-num_list[i]*max))

    # Show completed image file
    img.show()
    # Save file
    img.save("imp1_" + difficulty + "_output.png")
    print("Created output file: imp1_" + difficulty + "_output.png")

start = time.time()

read_img("easy")
read_img("medium")
read_img("hard")

print(f'Implementation #1 took {time.time() - start} seconds to run!')