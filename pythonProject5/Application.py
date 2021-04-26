import streamlit as st
import cv2
import numpy as np
from colorthief import ColorThief
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm
from operator import itemgetter


color_thief = ColorThief('TheScream-mod2.jpg')
palette = color_thief.get_palette(color_count=6)

hex_array=[]

for i in palette:
    hexa=list(i)
    hex_array.append(hexa)

#print(hex_array)

hex_array=sorted(hex_array,key=itemgetter(0),reverse=True)

st.write("LUT image to apply the style on: Unity uses 1024x32 LUT image")

path=st.file_uploader("Upload LUT",type=["jpg","png"])

def QuantizeToGivenPalette(im, palette):
    """Quantize image to a given palette.

    The input image is expected to be a Numpy array.
    The palette is expected to be a list of R,G,B values."""

    # Calculate the distance to each palette entry from each pixel
    distance = np.linalg.norm(im[:,:,None] - palette[None,None,:], axis=3)

    # Now choose whichever one of the palette colours is nearest for each pixel
    palettised = np.argmin(distance, axis=2).astype(np.uint8)

    return palettised

