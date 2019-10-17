"""Contract #2: Platformer Level Generator

This script will attempt to solve contract #2, using PIL to load and render out the images,
as PIL > PyGame for these sorts of image editing tasks
"""

"""TODO:
+ Add support for Wells and Shrines
+ Add final graphics
+ Add argparse support
* Add checking to see if the level already has an item at the chosen position
+ Add support for colour palettes 
"""

from PIL import Image
from enum import auto, Enum
import argparse
import random
from opensimplex import OpenSimplex
from datetime import datetime


class LevelData(Enum):
    GRASS = auto()
    SKY = auto()
    DIRT = auto()
    WATER = auto()
    POT = auto()
    STONE = auto()


__author__ = "Matthew Shaw"

size_of_tiles = (16, 16)
size_of_level = (100, 100)

grass_height = 5

dirtThreshold = 0.5

LevelImages = ["" for x in range(len(LevelData))]

# Create perlin noise generator with seed set to the current utc time
perlinGenerator = OpenSimplex(int(round((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())))

# Load all the images, by referencing the enum name
for item in LevelData:
    try:
        LevelImages[item.value-1] = Image.open("data/" + item.name.lower() + ".png")
    except FileNotFoundError:
        print("File data/" + item.name.lower() + ".png could not be found. Is it in the correct folder, and named accordingly?")
        exit(1)


# Create the final image to export
level = Image.new('RGB', (size_of_tiles[0] * size_of_level[0], size_of_tiles[1] * size_of_level[1]), (82, 192, 255))

# Create a list to hold the final level data, and initialise everything to sky
level_data = [[LevelData.SKY for y in range(size_of_level[1])] for x in range(size_of_level[0])]

for x in range(size_of_level[0]):
    for y in range(size_of_level[1]):
        # Check if we need to place terrain
        if (perlinGenerator.noise2d(x/20, y/20) + 1) / 2 < dirtThreshold:

            # If it is sky above here, then place grass
            if (perlinGenerator.noise2d(x/20, (y-1)/20) + 1) / 2 >= dirtThreshold:
                level_data[x][y] = LevelData.GRASS
            else:
                level_data[x][y] = LevelData.DIRT

            if level_data[x][y] == LevelData.DIRT and level_data[x][y-1] == LevelData.DIRT and level_data[x][y-2] == LevelData.DIRT or level_data[x][y-1] == LevelData.STONE:
                level_data[x][y] = LevelData.STONE

# Add water
for i in range(10000):
    point = [random.randrange(0, size_of_level[0]), random.randrange(0, size_of_level[1])]
    try:
        if level_data[point[0]][point[1]] == LevelData.SKY and level_data[point[0]][point[1]+1] == LevelData.GRASS:
            # We found sky, start making water
            while True:
                try:
                    while level_data[point[0]][point[1]+1] == LevelData.SKY or level_data[point[0]][point[1]+1] == LevelData.WATER:
                        point[1] += 1
                        level_data[point[0]][point[1]] = LevelData.WATER

                    if level_data[point[0] + 1][point[1] + 1] == LevelData.SKY and level_data[point[0]][point[1]] == LevelData.GRASS:
                        level_data[point[0]+1][point[1]] = LevelData.WATER
                        level_data[point[0]+1][point[1]+1] = LevelData.WATER
                        point[0] += 1
                        point[1] += 1

                    if level_data[point[0] - 1][point[1] + 1] == LevelData.SKY and level_data[point[0]][point[1]] == LevelData.GRASS:
                        level_data[point[0] - 1][point[1]] = LevelData.WATER
                        level_data[point[0] - 1][point[1] + 1] = LevelData.WATER
                        point[0] -= 1
                        point[1] += 1

                    if level_data[point[0]+1][point[1]] == LevelData.SKY:
                        point[0] += 1
                        level_data[point[0]][point[1]] = LevelData.WATER
                    elif level_data[point[0]-1][point[1]] == LevelData.SKY:
                        point[0] -= 1
                        level_data[point[0]][point[1]] = LevelData.WATER
                    else:
                        break
                except IndexError:
                    break
    except IndexError:
        continue


for i in range(10000):
    point = [random.randrange(0, size_of_level[0]), random.randrange(0, size_of_level[1])]
    try:
        if level_data[point[0]][point[1]] == LevelData.SKY and level_data[point[0]][point[1] + 1] == LevelData.GRASS:
            level_data[point[0]][point[1]] = LevelData.POT
    except ValueError:
        continue
    except IndexError:
        continue

# Write the level data to the image
for x in range(size_of_level[0]):
    for y in range(size_of_level[1]):
        level.paste(LevelImages[level_data[x][y].value - 1], (x * size_of_tiles[0], y * size_of_tiles[1]), LevelImages[level_data[x][y].value - 1].convert('RGBA'))

level.show()

# 7582 ♥
