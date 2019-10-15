"""Contract #2: Platformer Level Generator

This script will attempt to solve contract #2, using PIL to load and render out the images,
as PIL > PyGame for these sorts of image editing tasks
"""

"""TODO:
+ Add support for Water, Pools and Pots
+ Add final graphics
+ Add argparse support
+ Add support for multiple level types
* Add checking to see if the level already has an item at the chosen position
+ Add support for colour palettes 
"""

from PIL import Image
from enum import auto, Enum
import argparse
import random

class LevelData(Enum):
    GRASS = auto()
    SKY = auto()
    DIRT = auto()
    PITFALLLEFT = auto()
    PITFALLRIGHT = auto()
    WELLLEFT = auto()
    WELLRIGHT = auto()
    SHRINE = auto()


__author__ = "Matthew Shaw"

size_of_tiles = (16, 16)
size_of_level = (30, 10)

generator_mode = "mario"
mario_jump_height = 5
mario_jump_length = 6

LevelImages = ["" for x in range(len(LevelData))]

# Load all the images, by referencing the enum name
for item in LevelData:
    try:
        LevelImages[item.value-1] = Image.open("data/" + item.name.lower() + ".png")
    except FileNotFoundError:
        print("File data/" + item.name.lower() + ".png could not be found. Is it in the correct folder, and named accordingly?")
        exit(1)


# Create the final image to export
level = Image.new('RGB', (size_of_tiles[0] * size_of_level[0], size_of_tiles[1] * size_of_level[1]))

# Create a list to hold the final level data
level_data = [["" for y in range(size_of_level[1])] for x in range(size_of_level[0])]

# Create a base terrain (grass level is at 3, below is dirt, above is sky)
for x in range(len(level_data)):
    for y in range(len(level_data[0])):
        if y < 3:
            level_data[x][y] = LevelData.SKY
        elif y == 3:
            level_data[x][y] = LevelData.GRASS
        else:
            level_data[x][y] = LevelData.DIRT

# Create level data here
# shrines
# water
# pools
# pots

if random.random() < 0.5:  # Generate pitfalls
    pitfall_width = random.randrange(2, mario_jump_length)
    pitfall_y = 3
    pitfall_x = random.randint(0, size_of_level[0] - pitfall_width)
    level_data[pitfall_x][pitfall_y] = LevelData.PITFALLLEFT
    level_data[pitfall_width + pitfall_x - 1][pitfall_y] = LevelData.PITFALLRIGHT
    for i in range(pitfall_width - 2):
        level_data[i+pitfall_x + 1][pitfall_y] = LevelData.DIRT

if random.random() < 0.5:  # Generate Shrines
    shrine_x = random.randint(0, size_of_level[0])
    shrine_y = 2
    level_data[shrine_x][shrine_y] = LevelData.SHRINE
    pass

if random.random() < 0.5:  # Generate Wells
    well_x = random.randint(0, size_of_level[0] - 2)
    well_y = 3
    level_data[well_x][well_y] = LevelData.WELLLEFT
    level_data[well_x + 1][well_y] = LevelData.WELLRIGHT

if random.random() < 0.5:  # Generate Water
    pass

if random.random() < 0.5:  # Generate Pools
    pass

if random.random() < 0.5:  # Generate Pots
    pass

# Render out the level data to the final level image
for x in range(size_of_level[0]):
    for y in range(size_of_level[1]):
        level.paste(LevelImages[level_data[x][y].value - 1], (x * size_of_tiles[0], y * size_of_tiles[1]))

# Show and save
level.show()
level.save("level.png")

# 7582 ♥
