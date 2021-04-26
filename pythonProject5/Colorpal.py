import cv2
import numpy as np
import colorthief
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm
from operator import itemgetter
import streamlit as st


#path=r'generatePNG.png'

#im = cv2.imread(path, cv2.IMREAD_GRAYSCALE);
#im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR);
#im_color = applyCustomColorMap(im);

#cv2.imwrite('LUT_algae.jpg', im_color)
#cv2.imshow("Pseudo Colored Image", im_color);

from colorthief import ColorThief

colors=[6]


color_thief = ColorThief('paperheader.jpg')
# get the dominant color
#dominant_color = color_thief.get_color(quality=1)
#print(dominant_color)
# build a color palette


    #print(hex_array)



#print(palette)




path='Bleach Bypass.png'

def QuantizeToGivenPalette(im, palette):
    """Quantize image to a given palette.

    The input image is expected to be a Numpy array.
    The palette is expected to be a list of R,G,B values."""

    # Calculate the distance to each palette entry from each pixel
    distance = np.linalg.norm(im[:,:,None] - palette[None,None,:], axis=3)

    # Now choose whichever one of the palette colours is nearest for each pixel
    palettised = np.argmin(distance, axis=2).astype(np.uint8)

    return palettised




hex_array = []
for color in colors:
    palette = color_thief.get_palette(color_count=color)
    for i in palette:
        hexa = list(i)
        hex_array.append(hexa)

    #print(hex_array)

    hex_array = sorted(hex_array, key=itemgetter(0), reverse=True)
    im = cv2.imread(path, cv2.IMREAD_COLOR)

    inPalette = np.array(hex_array, dtype=np.uint8)

    r = QuantizeToGivenPalette(im, inPalette)
    lut = np.zeros((color, 3), dtype=np.uint8)
    # automate process

    for i in range(0, color-1):
        lut[i] = hex_array[i]

    # ----------------------
    result = lut[r]

    cv2.imwrite('result312'+str(color)+'.png', result)
