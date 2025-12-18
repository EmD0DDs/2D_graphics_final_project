# color inversion
# formula for inversion from - https://www.geeksforgeeks.org/python/python-color-inversion-using-pillow/#
# formula - inversion = maxRGB - pixelRGB

from PIL import Image

image = Image.open("./rainbow_tile.jpg")
raster = image.load()

# want to invert the colors in an image 
for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        r = 255 - pixel[0]
        g = 255 - pixel[1]
        b = 255 - pixel[2]

        raster[x, y] = (r, g, b)

image.save("inverted_rainbow_tile.png")