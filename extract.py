from PIL import Image
import random

key = 2026

# 0 = red, 1 = green, 2 = blue
colourPlane = 1

# least sig bit
significantBit = 7

stegoImage = "stego-image.bmp"


image = Image.open(stegoImage).convert("RGB")

dimensions = image.size
pixels = image.load()

total_pixels = dimensions[0] * dimensions[1]

shuffledIndices = list(range(total_pixels))

random.seed(key)
random.shuffle(shuffledIndices)

extractedBits = []

for i in shuffledIndices:

    x = i % dimensions[0]
    y = i // dimensions[0]

    p = format(pixels[x, y][colourPlane], 'b').zfill(8)

    extractedBits.append(p[significantBit])

extractedLengthBits = extractedBits[:14]
extractedLength = int(''.join(extractedLengthBits), 2)

extractedSecretASCII = []

for i in range(extractedLength):

    a = 0

    for j in range(7):
        a += int(extractedBits[14 + i * 7 + j]) * (2 ** (6 - j))

    extractedSecretASCII.append(chr(a))

secret = ''.join(extractedSecretASCII)
print(secret)