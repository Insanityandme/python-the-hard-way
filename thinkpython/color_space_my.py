import sys
from visual import *

def main():

    from color_list import *
    color_dict = make_color_dict()
    colors, rgbs = read_colors()

    for rgb, names in rgbs:
        print vector(rgb)
    

if __name__ == '__main__':
    main()
