import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./rainbow_tile.jpg")

plt.imshow(image)
plt.title("image in BGR Mode")
plt.axis("off")
plt.show()

rgb_image = image[...,::-1]

plt.imshow(rgb_image)
plt.title("image in RGB Mode")
plt.axis("off")
plt.show()

r, g, b = cv2.split(rgb_image)

kernel = np.array([
    [1/16, 1/8, 1/16],
    [1/8, 1/4, 1/8],
    [1/16, 1/8, 1/16]
    ])

plt.figure(figsize=(10, 3))
plt.subplot(1, 3, 1)
plt.imshow(r, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(g, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(b, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.show()