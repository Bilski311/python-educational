from collections import namedtuple

sizes = 'S M L'.split()
colors = 'white black'.split()

Shirt = namedtuple('Shirt', ['size', 'color'])

for shirt in (Shirt(size, color) for size in sizes for color in colors):
    print(shirt)