from PIL import Image
import random


key = 2026

# 0 = red, 1 = green, 2 = blue
colourPlane = 1

# least sig bit
significantBit = 7

coverImage = "flowers.bmp"
secretFile = "secret.txt"

outputImage = "stego-image.bmp"



image = Image.open(coverImage).convert("RGB")

dimensions = image.size

pixels = image.load()

with open(secretFile, "r", encoding="utf-8") as f:
    secret = f.read()

total_pixels = dimensions[0] * dimensions[1]

sbits = ''.join(format(ord(char), 'b').zfill(7) for char in secret)

lbits = format(len(secret), 'b').zfill(14)

bits = lbits + sbits

if len(bits) > total_pixels:
    raise Exception("Image does not have enough capacity")


shuffledIndices = list(range(total_pixels))

random.seed(key)
random.shuffle(shuffledIndices)

def modify_pixel(pixel, plane, bit, modifier):

    m = modifier * (2 ** (7 - bit))

    r = pixel[0] + m if plane == 0 else pixel[0]
    g = pixel[1] + m if plane == 1 else pixel[1]
    b = pixel[2] + m if plane == 2 else pixel[2]

    return (r, g, b)


for i in range(len(bits)):

    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]

    p = format(pixels[x, y][colourPlane], 'b').zfill(8)

    if p[significantBit] == '0' and bits[i] == '1':
        pixels[x, y] = modify_pixel(
            pixels[x, y],
            colourPlane,
            significantBit,
            1
        )

    elif p[significantBit] == '1' and bits[i] == '0':
        pixels[x, y] = modify_pixel(
            pixels[x, y],
            colourPlane,
            significantBit,
            -1
        )

image.save(outputImage)

print("Embedding complete. Output saved as:", outputImage)