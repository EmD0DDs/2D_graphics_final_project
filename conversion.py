import numpy as np
import math 
from PIL import Image
from test import *

image = Image.open("./rainbow.jpg")
raster = image.load()

# want to test conversion with formula from https://mk.bcgsc.ca/colorblind/math.mhtml

# 1.1 - rgb to linear rgb
def rgb_to_linear_rgb(values):
    # need to normalize and convert to linear rgb
    for i in range(len(values)):
        values[i] = float(values[i] / 255)

        if values[i] <= 0.04045:
            values[i] /= 12.92
        else:
            values[i] = float(((values[i] + 0.055) / 1.055) ** 2.4)

    return values

def linear_rgb_to_rgb(values):
    for i in range(len(values)):
        if values[i] <= 0.0031308:
            values[i] *= 12.92
            values[i] = int(values[i]*255)
        else:
            values[i] = values[i] ** (1/2.4)

            values[i] *= 1.055
            values[i] -= 0.055
            values[i] *= 255
            values[i] = int(values[i])
    return values

# 1.2 - linear rgb to xyz
def linear_rgb_to_xyz(values):
    xyz = np.array([[0.4124564, 0.3575761, 0.1804375],
                    [0.2126729, 0.7151522, 0.0721750],
                    [0.0193339, 0.1191920, 0.9503041]])
    
    xyz_values = xyz @ values
    return xyz_values

def xyz_to_linear_rgb(values):
    inverse_xyz = np.array([[3.24045484, -1.5371389, -0.49853155],
                            [-0.96926639, 1.8760109, 0.04155608],
                            [0.05564342, -0.2040259, 1.05722516]])
    linear_rgb = inverse_xyz @ values
    return linear_rgb

# 1.3 - xyz to lms
def xyz_to_lms(values):
    # normalize values to lms 65 to make transformations easier later
    lms65 = np.array([[0.4002, 0.7076, -0.0808],
                      [-0.2263, 1.1653, 0.0457],
                      [0, 0, 0.9182]])
    
    lms65_values = lms65 @ values
    return lms65_values

def lms_to_xyz(values):
    inverse_lms65 = np.array([[1.8600666, -1.1294801, 0.2198983], 
                              [0.3612229, 0.6388043, 0],
                              [0, 0, 1.089087]])
    xyz_values = inverse_lms65 @ values
    return xyz_values

# 1.4 - color correction
def protanopia(values):
    prot = np.array([[0, 1.05118294, -0.05116099],
                     [0, 1, 0],
                     [0, 0, 1]])
    prot_values = prot @ values
    return prot_values

def deuteranopia(values):
    deut = np.array([[1, 0, 0],
                     [0.9513092, 0, 0.04866992],
                     [0, 0, 1]])
    deut_values = deut @ values
    return deut_values

def tritanopia(values):
    tritan = np.array([[1, 0, 0],
                       [0, 1, 0],
                       [-0.86744736, 1.86727089, 0]])
    tritan_values = tritan @ values
    return tritan_values
    


for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        rgb = np.array([r, g, b])
        lrgb = rgb_to_linear_rgb(rgb)
        xyz = linear_rgb_to_xyz(lrgb)
        lms = xyz_to_lms(xyz)

        deut_values = deuteranopia(lms)

        #CONVERT BACK TO RGB
        deut_values = lms_to_xyz(deut_values)
        deut_values = xyz_to_linear_rgb(deut_values)
        deut_values = linear_rgb_to_rgb(deut_values)
        


        raster[x, y] = (int(deut_values[0]), int(deut_values[1]), int(deut_values[2]))



image.save("./deut_rainbow.png")