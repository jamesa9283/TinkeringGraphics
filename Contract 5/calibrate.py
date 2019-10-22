from PIL import Image
import colorsys

__author__ = "Matthew Shaw"

# Load in the reference conversion image
img = Image.open("calibration.png").convert("RGB")
imgData = img.load()

# Create a list for every type of colour blindness, to read the hue values into.
Normal = []
deuteranomaly = []
protanomaly = []
protanopia = []
deuteranopia = []
tritanopia = []
tritanomaly = []

# For every different type of colour blindness, convert it from 0-255 to 0-1, and append the hue to the list
for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 0]]
    Normal.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 21]]
    deuteranomaly.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0] * 255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 42]]
    protanomaly.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0] * 255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 63]]
    protanopia.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0] * 255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 84]]
    deuteranopia.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0] * 255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 103]]
    tritanopia.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0] * 255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 118]]
    tritanomaly.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0] * 255)))

# Open an output file, and write out all of the lists, in a comma-separated format
with open("blindnessValues.txt", 'w') as file:
    file.write(','.join([str(x) for x in deuteranomaly]) + "\n")
    file.write(','.join([str(x) for x in protanomaly]) + "\n")
    file.write(','.join([str(x) for x in protanopia]) + "\n")
    file.write(','.join([str(x) for x in deuteranopia]) + "\n")
    file.write(','.join([str(x) for x in tritanopia]) + "\n")
    file.write(','.join([str(x) for x in tritanomaly]) + "\n")






