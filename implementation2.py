import math
import time

# Interpret raw visual data from a text file
# Implementation #2
# Presenting visual data as a text file

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

    # Create array that will store the characters
    pixels = []

    # Loop through list and find highest value
    max = 0
    for i in range(len(num_list)):
        if num_list[i] > max:
            max = num_list[i]
    # Divide 255 by max to determine factor that the raw numbers should be multiplied by 
    max = 255 / max

    # Determine size of image
    # Width is guaranteed 256 for easy and medium, 512 for hard
    if difficulty == "hard":
        width = 512
    else:
        width = 256
    height = int(len(num_list) / width)

    # For the range of the height
    for i in range(height):
        # Create array that will store characters for this current row
        temp = []
        # Nested for loop that will add characters to array
        # For range of the width
        for j in range(width):
            # Find the next needed number in num_list
            # Multiply by max factor so numbers scale from 0-255
            pixel = int(num_list[i*width+j]*max)
            # Add characters to temp array based on the intensity
            if pixel > 200:
                temp.append("██")
            elif pixel > 150:
                temp.append("▒▒")
            elif pixel > 90:
                temp.append("░░")
            elif pixel > 50:
                temp.append("--")
            else:
                temp.append("  ")
        # Add temp array to the pixels array as a new "row" of the image.
        pixels.append(temp)

    # Open file to print list to
    output_file = open("imp2_" + difficulty + "_output.txt","w",encoding="utf-8")

    # Print each list inside of pixels with no separation between values to output_file
    for i in pixels:
        print(*i,sep="",file= output_file)

    # Close file
    output_file.close()
    print("Created output file: imp2_" + difficulty + "_output.txt")

start = time.time()

read_img("easy")
read_img("medium")
read_img("hard")

print(f'Implementation #2 took {time.time() - start} seconds to run!')