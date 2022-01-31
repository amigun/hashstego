import sys
from PIL import Image
from hashlib import sha256

def hash(input_value):
    return sha256(str(input_value).encode()).hexdigest()

def part(input_value):
    for i in range(0, len(input_value), 2):
        yield input_value[i:i + 2]

def rgb2hex(r, g, b):
    return int('{:02x}{:02x}{:02x}'.format(r, g, b), 16)

filename, path_to_image, password = sys.argv

text = ''

image = Image.open(path_to_image)

width, height = image.size
pixels = image.load()

not_hex = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for nh in not_hex:
    password = password.replace(nh, ' ')

hex2int = []

for nibble in password.split():
    hex2int.append(int(nibble, 16))

nibbles = []

for coord in list(part(hex2int)):
    nibbles.append(hash(rgb2hex(*pixels[coord[0], coord[1]]) * rgb2hex(*pixels[coord[0] + 1, coord[1]]))[:2])

for nibble in nibbles:
    text += chr(int(nibble, 16))

print(text)
