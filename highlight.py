from PIL import Image
import random

key = 2026
coverImage = "flowers.bmp"
outputImage = "highlighted-image.bmp"

image = Image.open(coverImage).convert("RGB")
pixels = image.load()

dimensions = image.size

total_pixels = dimensions[0] * dimensions[1]

shuffledIndices = list(range(total_pixels))

random.seed(key)
random.shuffle(shuffledIndices)

for i in range(10000):

    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]

    pixels[x, y] = (255, 0, 0)

image.save(outputImage)

print("Highlighted image saved")
