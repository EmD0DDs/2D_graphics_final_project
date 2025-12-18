# want to experiment with different types of color blindness
"""
deuteranomaly - green looks more red
protanomaly - some reds look green and duller
protanopia and deuteranopia - can't tell difference between red and green
tritanomaly - can't tell difference between blue or green and cant tell diff between red and yellow
tritanopia - cant tell diff between b and g, purple and red, yellow and pink plus duller colors
complete color blindness - black and white vision
"""

from PIL import Image

image = Image.open("./rainbow_tile.jpg")
raster = image.load()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        k = int(.2 * r + .7 * g + .1 * b)

        raster[x, y] = (k, k, k)


image.save("ach_rainbow_tile.png")