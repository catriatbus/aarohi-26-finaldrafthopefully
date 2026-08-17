"""
Remove a near-gray background from an image and save as PNG with transparency.
Usage:
    python scripts/remove_bg.py input.jpg output.png --r 200 --g 200 --b 200 --t 60

Arguments:
    input: path to the source image (any Pillow-supported format)
    output: path to write the PNG with alpha
Options:
    --r, --g, --b : approximate RGB color to make transparent (default 200,200,200)
    --t : tolerance (0-255) for color distance (default 60)

Note: This is a simple color-threshold remover. For complex edges, use more advanced tools.
"""
from PIL import Image
import sys
import argparse
import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--r', type=int, default=200)
    parser.add_argument('--g', type=int, default=200)
    parser.add_argument('--b', type=int, default=200)
    parser.add_argument('--t', type=int, default=60, help='tolerance')
    args = parser.parse_args()

    try:
        im = Image.open(args.input).convert('RGBA')
    except Exception as e:
        print('Error opening image:', e)
        sys.exit(1)

    datas = im.getdata()
    newData = []
    target = (args.r, args.g, args.b)
    tol = args.t

    def dist(c1, c2):
        return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

    for item in datas:
        # item is (r,g,b,a)
        r,g,b,a = item
        if dist((r,g,b), target) <= tol:
            # make pixel transparent
            newData.append((r, g, b, 0))
        else:
            newData.append(item)

    im.putdata(newData)
    try:
        im.save(args.output, 'PNG')
        print('Saved:', args.output)
    except Exception as e:
        print('Error saving image:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
