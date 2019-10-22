"""Contract #2: Platformer Level Generator

This script will attempt to solve contract #2, using PIL to load and render out the images,
as PIL > PyGame for these sorts of image editing tasks
"""

"""TODO:
+ Add support for Wells and Shrines
+ Add final graphics
+ Add argparse support
+ Add support for colour palettes 
"""

from PIL import Image
from enum import auto, Enum
import random
from opensimplex import OpenSimplex
from datetime import datetime


class LevelTiles(Enum):
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

# Create perlin noise generator with seed set to the current utc time (changing number make good random seed)
perlin_generator = OpenSimplex(int(round((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())))

LevelImages = ["" for x in range(len(LevelTiles))]

# Load all the images, by referencing the enum name
for item in LevelTiles:
    try:
        LevelImages[item.value-1] = Image.open("data/" + item.name.lower() + ".png")
    except FileNotFoundError:
        print("File data/" + item.name.lower() + ".png could not be found. Is it in the correct folder, and named accordingly?")
        exit(1)

# Create the final image to export
level = Image.new('RGB', (size_of_tiles[0] * size_of_level[0], size_of_tiles[1] * size_of_level[1]), (82, 192, 255))

# Create a list to hold the final level data, and initialise everything to sky
level_data = [[LevelTiles.SKY for y in range(size_of_level[1])] for x in range(size_of_level[0])]

# Create the base dirt/stone
for x in range(size_of_level[0]):
    for y in range(size_of_level[1]):
        # Check if we need to place terrain
        if ((perlin_generator.noise2d(x/20, y/20) + perlin_generator.noise2d(x/50, y/50) + 1) / 2) < dirtThreshold:

            # If it is sky above here, then place grass
            if ((perlin_generator.noise2d(x/20, (y-1)/20) + perlin_generator.noise2d(x/50, (y-1)/50) + 1) / 2) >= dirtThreshold:
                level_data[x][y] = LevelTiles.GRASS
            else:
                level_data[x][y] = LevelTiles.DIRT

            # If the three tiles above the current tile are all dirt, or the tile above is stone, make the current tile stone
            if level_data[x][y] == LevelTiles.DIRT and level_data[x][y - 1] == LevelTiles.DIRT and level_data[x][y - 2] == LevelTiles.DIRT or level_data[x][y - 1] == LevelTiles.STONE:
                level_data[x][y] = LevelTiles.STONE

# Add water
for i in range(1000):
    point = [random.randrange(0, size_of_level[0]), random.randrange(0, size_of_level[1])]
    try:
        if level_data[point[0]][point[1]] == LevelTiles.STONE and level_data[point[0]][point[1] + 1] == LevelTiles.SKY:
            # We found sky, start making water
            while True:
                try:
                    # While the tile below the water is sky or water, create water below the current tile
                    while level_data[point[0]][point[1]+1] == LevelTiles.SKY or level_data[point[0]][point[1] + 1] == LevelTiles.WATER:
                        point[1] += 1
                        level_data[point[0]][point[1]] = LevelTiles.WATER

                    # If the tile down and to the right is sky, and the tile below is water, make the right and down-right tile water
                    if level_data[point[0] + 1][point[1] + 1] == LevelTiles.SKY and level_data[point[0]][point[1]] == LevelTiles.GRASS:
                        level_data[point[0]+1][point[1]] = LevelTiles.WATER
                        level_data[point[0]+1][point[1]+1] = LevelTiles.WATER
                        point[0] += 1
                        point[1] += 1

                    # If the tile down and to the left is sky, and the tile below is water, make the left and down-left tile water
                    elif level_data[point[0] - 1][point[1] + 1] == LevelTiles.SKY and level_data[point[0]][point[1]] == LevelTiles.GRASS:
                        level_data[point[0] - 1][point[1]] = LevelTiles.WATER
                        level_data[point[0] - 1][point[1] + 1] = LevelTiles.WATER
                        point[0] -= 1
                        point[1] += 1

                    # If the tile to the right is sky, make the tile to the right water
                    elif level_data[point[0]+1][point[1]] == LevelTiles.SKY:
                        point[0] += 1
                        level_data[point[0]][point[1]] = LevelTiles.WATER

                    # If the tile to the left is sky, make the tile to the left water
                    elif level_data[point[0]-1][point[1]] == LevelTiles.SKY:
                        point[0] -= 1
                        level_data[point[0]][point[1]] = LevelTiles.WATER
                    else:
                        break
                except IndexError:
                    break
    except IndexError:
        continue

# Add pots
for i in range(1000):
    point = [random.randrange(0, size_of_level[0]), random.randrange(0, size_of_level[1])]
    try:
        if level_data[point[0]][point[1]] == LevelTiles.SKY and level_data[point[0]][point[1] + 1] == LevelTiles.GRASS:
            level_data[point[0]][point[1]] = LevelTiles.POT
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
