import sys, random
from PIL import Image
from hashlib import sha256

def hash(input_value):
    return sha256(str(input_value).encode()).hexdigest()

def str2hex(input_value):
    return [hex(ord(input_value[symb]))[2:] for symb in range(len(input_value))]

def rgb2hex(r, g, b):
    return int('{:02x}{:02x}{:02x}'.format(r, g, b), 16)

filename, path_to_image, text = sys.argv

password = ''

image = Image.open(path_to_image)

width, height = image.size
pixels = image.load()

if width < 100 or height < 100:
    print('Error: The image must be 100 or more pixels width and height!')

nibbles = str2hex(text)

not_hex = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for nibble in nibbles:
    stop = False

    for row in range(height - 1):
        for col in range(width - 1):
            if hash(rgb2hex(*pixels[col, row]) * rgb2hex(*pixels[col + 1, row]))[:2] == nibble:
                password += f'{hex(col)[2:]}{random.choice(not_hex)}{hex(row)[2:]}{random.choice(not_hex)}'

                stop = True

                break
        if stop:
            break

print(password[:-1])
