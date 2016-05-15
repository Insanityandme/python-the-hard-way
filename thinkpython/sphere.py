from visual import *
import sys
from textwrap import wrap


# rgb is a hexadecimal value, example: #ffffff
def convert_to_rgb(hex):
    # Removes the # through the strip function
    hex = hex.strip('#')
    # Divides the hex value into three seperate parts
    r, g, b = wrap(hex, 2)
    # Converts the hex value into decimals
    r, g, b = int(r, 16), int(g, 16), int(b, 16)

    return r, g, b


def draw_spheres(rgbs, radius=10):
    for hex, names in rgbs:
        pos = convert_to_rgb(hex)
        r, g, b = convert_to_rgb(hex)
        d = float(255)
        color = r/d, g/d, b/d
        sphere(pos=pos, radius=radius, color=color)


def main():
    from color_list import read_colors

    colors, rgbs = read_colors()

    scene.range = (256, 256, 256)
    scene.center = (128, 128, 128)

    draw_spheres(rgbs, 10)

if __name__ == '__main__':
    main()
