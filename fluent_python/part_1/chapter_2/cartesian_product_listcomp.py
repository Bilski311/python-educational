from collections import namedtuple

sizes = 'S M L'.split()
colors = 'white black'.split()

Shirt = namedtuple('Shirt', ['size', 'color'])
shirts = [Shirt(size, color) for size in sizes for color in colors]

for shirt in shirts:
    print(shirt)