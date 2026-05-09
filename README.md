# Image Steganography Homework

## Course

Data Security

## Description

This project implements a simple image steganography system using Python and the Pillow library.

The system hides a secret text message inside a BMP image by modifying one bit inside a selected RGB colour channel.

The hidden message can later be extracted using the same:

* key,
* colour plane,
* bit position.

The project demonstrates:

* Least Significant Bit (LSB) steganography,
* pseudo-random pixel selection,
* image-based hidden communication.

---

# Project Structure

```text
steganography-hw/
├── embed.py
├── extract.py
├── highlight.py
├── secret.txt
├── requirements.txt
├── flowers.bmp
├── dice.bmp
├── tiger.bmp
├── stego-image.bmp
├── highlighted-image.bmp
├── report.pdf
└── README.md
```

---

# Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Required package:

```text
pillow
```

---

# Configuration

The system uses the following configuration:

```python
key = 2026
colourPlane = 1
significantBit = 7
```

Explanation:

* `key`

  * Generates the pseudo-random pixel order.

* `colourPlane`

  * `0` = red
  * `1` = green
  * `2` = blue

* `significantBit`

  * `7` = least significant bit (LSB)
  * `0` = most significant bit (MSB)

---

# Running the Program

## 1. Embed the Secret Message

```bash
python embed.py
```

Expected output:

```text
Embedding complete. Output saved as: stego-image.bmp
```

This creates:

```text
stego-image.bmp
```

---

## 2. Extract the Secret Message

```bash
python extract.py
```

Expected output:

```text
Meet me at the lab after the lecture. This message is hidden using image steganography.
```

---

## 3. Highlight Used Pixels

```bash
python highlight.py
```

This creates:

```text
highlighted-image.bmp
```

The highlighted image visualizes the pseudo-random pixel distribution used during embedding.

---

# How the System Works

## Embedding Process

1. Open the cover image.
2. Read the secret message.
3. Convert the message into 7-bit ASCII.
4. Store the message length using 14 bits.
5. Generate a shuffled pixel order using a shared key.
6. Modify one selected bit inside one RGB colour channel.
7. Save the stego-image.

---

## Extraction Process

1. Open the stego-image.
2. Generate the same shuffled pixel order.
3. Read the selected bit from each selected pixel.
4. Read the first 14 bits as the message length.
5. Reconstruct the original ASCII message.
6. Print the recovered secret.

---

# Capacity Formula

```text
pixels = width × height
capacity_bits = pixels × bits_per_pixel
capacity_bytes = capacity_bits / 8
message_bits = 14 + 7 × number_of_characters
```

This implementation stores:

```text
1 bit per pixel
```

because only one colour channel is modified.

---

# Security Notes

## Advantages

* Hidden message is difficult to notice visually.
* Pseudo-random pixel order increases secrecy.
* LSB modification minimizes visible distortion.

## Weaknesses

* Vulnerable to compression and resizing.
* Hidden data is not encrypted.
* Using incorrect parameters prevents successful extraction.

---

# Experimental Observations

* Using `bit_position = 7` produced almost invisible changes.
* Using `bit_position = 0` visibly corrupted the image.
* The green channel produced the best visual quality.
* Complex images such as `tiger.bmp` hide modifications more effectively.

---

# Author

Jon Zylfiu
