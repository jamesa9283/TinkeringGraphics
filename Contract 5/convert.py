import colorsys
from PIL import Image
"""Contract #5, Completed by Matthew Shaw"""


def normal_to_colour_blind(_normal_colour: (int, int, int), conversion_list: list) -> (int, int, int):
    normal_colour = [x/255 for x in _normal_colour]
    normal_hsv = colorsys.rgb_to_hsv(normal_colour[0], normal_colour[1], normal_colour[2])
    blind_index = int(round(normal_hsv[0] * 173))
    blind_hue = conversion_list[blind_index]
    blind_colour = colorsys.hsv_to_rgb(blind_hue/255, normal_hsv[1], normal_hsv[2])
    return tuple([int(round(x*255)) for x in blind_colour])


for i in range(6):
    mode = i  # Deuteranomaly Protanomaly Protanopia Deuteranopia Tritanopia Tritanomaly

    values = []
    valuesstr = tuple(open("blindnessValues.txt", 'r'))[mode]

    values = [int(x) for x in valuesstr.split(',')]

    normal = Image.open("test.jpg").convert("RGB")
    normal_data = normal.load()
    for x in range(normal.size[0]):
       for y in range(normal.size[1]):
            normal_data[x,y] = normal_to_colour_blind(normal_data[x,y], values)

    normal.show()
    normal.save("converted"+str(i)+".png")
