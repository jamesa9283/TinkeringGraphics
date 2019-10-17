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
from opensimplex import OpenSimplex
from datetime import datetime


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
size_of_level = (100, 100)

grass_height = 5

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



for x in range(size_of_level[0]):
    for y in range(size_of_level[1]):
        level.paste(LevelImages[LevelData.DIRT.value-1] if perlinGenerator.noise2d(x/20, y/20) < 0.05 else LevelImages[LevelData.SKY.value-1], (x * size_of_tiles[0], y * size_of_tiles[1]))

level.show()

# 7582 ♥
