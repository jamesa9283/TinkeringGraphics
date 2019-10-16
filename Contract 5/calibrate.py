#15 colour, 4 white
from PIL import Image
import colorsys

img = Image.open("calibration.png").convert("RGB")
imgData = img.load()
Normal = []
Deuteranomaly = []
Protanomaly = []
Protanopia = []
Deuteranopia = []
Tritanopia = []
Tritanomaly = []
for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 0]]
    Normal.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 21]]
    Deuteranomaly.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 42]]
    Protanomaly.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 63]]
    Protanopia.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 84]]
    Deuteranopia.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 103]]
    Tritanopia.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

for x in range(img.size[0]):
    colour = [x/255 for x in imgData[x, 118]]
    Tritanomaly.append(int(round(colorsys.rgb_to_hsv(colour[0], colour[1], colour[2])[0]*255)))

with open("blindnessValues.txt", 'w') as file:
    file.write(','.join([str(x) for x in Deuteranomaly]) + "\n")
    file.write(','.join([str(x) for x in Protanomaly]) + "\n")
    file.write(','.join([str(x) for x in Protanopia]) + "\n")
    file.write(','.join([str(x) for x in Deuteranopia]) + "\n")
    file.write(','.join([str(x) for x in Tritanopia]) + "\n")
    file.write(','.join([str(x) for x in Tritanomaly]) + "\n")






