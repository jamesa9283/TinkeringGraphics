from PIL import Image
import argparse
import random

__author__ = "Matthew Shaw"

size_of_tiles = (16, 16)
size_of_level = (30, 10)

generator_mode = "mario"
mario_jump_height = 5
mario_jump_length = 6

# Locations of the image resources
grass_paths = ["data/grass.png"]
dirt_paths = ["data/dirt.png"]
sky_paths = ["data/sky.png"]
pitfall_paths = ["data/pitfallleft.png", "data/pitfallright.png"]
shrine_paths = ["data/shrine.png"]
well_paths = ["data/wellleft.png", "data/wellright.png"]
water_paths = ["data/water.png"]
pool_paths = ["data/poolleft.png", "data/poolright.png"]
pot_paths = ["data/pot.png"]

# Lists of the loaded images
grass_images = []
dirt_images = []
sky_images = []
pitfall_images = []
shrine_images = []
well_images = []
water_images = []
pool_images = []
pot_images = []

#Load all the images
for path in grass_paths:
    grass_images.append(Image.open(path))
for path in dirt_paths:
    dirt_images.append(Image.open(path))
for path in sky_paths:
    sky_images.append(Image.open(path))
for path in pitfall_paths:
    pitfall_images.append(Image.open(path))
for path in shrine_paths:
    shrine_images.append(Image.open(path))
for path in well_paths:
    well_images.append(Image.open(path))
for path in water_paths:
    water_images.append(Image.open(path))
for path in pool_paths:
    pool_images.append(Image.open(path))
for path in pot_paths:
    pot_images.append(Image.open(path))

# Create the final image to export
level = Image.new('RGB', (size_of_tiles[0] * size_of_level[0], size_of_tiles[1] * size_of_level[1]))

# Create a list to hold the final level data
level_data = [["" for y in range(size_of_level[1])] for x in range(size_of_level[0])]

# Create a base terrain (grass level is at 3, below is dirt, above is sky)
for x in range(len(level_data)):
    for y in range(len(level_data[0])):
        if y < 3:
            level_data[x][y] = "sky"
        elif y == 3:
            level_data[x][y] = "grass"
        else:
            level_data[x][y] = "dirt"

# Create level data here
# pitfalls
# shrines
# wells
# water
# pools
# pots

if random.random() < 0.5:  # Generate pitfalls
    pitfall_width = random.randrange(2, mario_jump_length)
    pitfall_y = 3
    pitfall_x = random.randint(0, size_of_level[0] - pitfall_width)
    print("adding pitfall with width", pitfall_width, "at", pitfall_x, pitfall_y)
    level_data[pitfall_x][pitfall_y] = "pitfallleft"
    level_data[pitfall_width + pitfall_x - 1][pitfall_y] = "pitfallright"
    for i in range(pitfall_width - 2):
        level_data[i+pitfall_x + 1][pitfall_y] = "dirt"

if random.random() < 0.5:  # Generate Shrines
    pass

if random.random() < 0.5:  # Generate Wells
    well_x = random.randint(0, size_of_level[0] - 2)
    well_y = 3
    level_data[well_x][well_y] = "wellleft"
    level_data[well_x + 1][well_y] = "wellright"

if random.random() < 0.5:  # Generate Water
    pass

if random.random() < 0.5:  # Generate Pools
    pass

if random.random() < 0.5:  # Generate Pots
    pass

# Render out the level data to the final level image
for x in range(size_of_level[0]):
    for y in range(size_of_level[1]):

        if level_data[x][y] == "sky":
            level.paste(sky_images[0], (x * size_of_tiles[0], y * size_of_tiles[1]))

        elif level_data[x][y] == "grass":
            level.paste(grass_images[0], (x * size_of_tiles[0], y * size_of_tiles[1]))

        elif level_data[x][y] == "dirt":
            level.paste(dirt_images[0], (x * size_of_tiles[0], y * size_of_tiles[1]))

        elif level_data[x][y] == "pitfallleft":
            level.paste(pitfall_images[0], (x * size_of_tiles[0], y * size_of_tiles[1]))

        elif level_data[x][y] == "pitfallright":
            level.paste(pitfall_images[1], (x * size_of_tiles[0], y * size_of_tiles[1]))

        elif level_data[x][y] == "wellleft":
            level.paste(well_images[0], (x * size_of_tiles[0], y * size_of_tiles[1]))

        elif level_data[x][y] == "wellright":
            level.paste(well_images[1], (x * size_of_tiles[0], y * size_of_tiles[1]))

# Show and save
level.show()
level.save("level.png")

# 7582 ♥
