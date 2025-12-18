# color change

from PIL import Image

image = Image.open("./rainbow_tile.jpg")
raster = image.load()

# want to switch colors in the photo
# red to green
# green to blue
# blue to red

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        all_red = (255, 0, 0)
        all_prple = (100, 0, 100)
        all_blue = (0, 0, 255)

        k = int(.2 * r + .7 * g + .1 * b)

        # if r > 100:
        #     raster[x, y] = all_prple
        # elif b > 100:
        #     raster[x, y] = all_red
        # elif g > 100:
        #     raster[x, y] = all_blue
        # else:
        #     raster[x, y] = (k, k, k)
        
        if b > 150:
            raster[x, y] = all_prple
        else:
            raster[x, y] = (k, k, k)

image.save("purple_rainbow_tile.png")
