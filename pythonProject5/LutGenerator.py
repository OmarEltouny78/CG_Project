import argparse
import numpy as np
import cv2
import sys
import math


def make_image_strip(samples=16, flipy=False):
    s = float(samples)
    mult = 255.0 / (s - 1)

    image = []

    if flipy:
        start = samples - 1
        end = -1
        step = -1
    else:
        start = 0
        end = samples
        step = 1
    p = 0.0
    for y in range(start, end, step):
        rows = []
        for x in range(0, samples * samples):
            rows.append([
                int(round((x / samples) * mult)),  # blue
                int(round(y * mult)),  # green
                int(round((x % samples) * mult))  # red
            ])
        image.append(rows)

        p += 1.0
    return image


def make_image_square(samples=16, flipy=False):
    s = float(samples)
    root = int(round(math.sqrt(samples)))
    mult = 255.0 / (s - 1)

    image = []

    if flipy:
        start = samples * root - 1
        end = -1
        step = -1
    else:
        start = 0
        end = samples * root
        step = 1
    p = 0.0
    for y in range(start, end, step):
        rows = []
        for x in range(0, samples * root):
            ri = (x % samples)
            gi = (y % samples)
            bi = int(y / samples * root) + int((x / samples) % root)
            rows.append([
                int(round(bi * mult)),  # blue
                int(round(gi * mult)),  # green
                int(round(ri * mult))  # red
            ])
        image.append(rows)
        p += 1.0
    return image


def write_image(image, path):
    image = np.array(image)
    try:
        if cv2.imwrite(path, image):
            print('>> Done!')
    except Exception as e:
        sys.exit(str(e))


#image1 = make_image_square(512)
image2 = make_image_square(64)
#write_image(image1, r"C:\Users\omart\OneDrive\Documents\New Unity Project Tak n\Assets\LUT\LUTstrip.png")
write_image(image2, r"C:\Users\omart\OneDrive\Documents\New Unity Project Tak n\Assets\LUT\LUTsquare.png")