from PIL import Image
import numpy as np

image = Image.open("./rainbow_tile.jpg")
raster = image.load()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        deut_matrix = np.array([[0.33066007, 0.66933993, 0],
                                [0.33066007, 0.66933993, 0],
                                [-0.02785538, 0.02785538, 1]])
        
        deut_values = deut_matrix @ pixel

        raster[x, y] = (int(deut_values[0]), int(deut_values[1]), int(deut_values[2]))



image.save("./deut_rainbow_tile.png")

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        prot_matrix = np.array([[0.170556992, 0.829443014, 0],
                                [0.170556991, 0.829443008, 0],
                                [-0.004517144, 0.004517144, 1]])
        
        prot_values = prot_matrix @ pixel

        raster[x, y] = (int(prot_values[0]), int(prot_values[1]), int(prot_values[2]))



image.save("./prot_rainbow_tile.png")

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x, y]

        tritan_matrix = np.array([[1, 0.1273989, -0.1273989],
                                [0, 0.8739093, 0.1260907],
                                [0, 0.8739093, 0.1260907]])
        
        tritan_values = tritan_matrix @ pixel

        raster[x, y] = (int(tritan_values[0]), int(tritan_values[1]), int(tritan_values[2]))



image.save("./tritan_rainbow_tile.png")