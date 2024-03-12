import numpy as np

# 1. Naming slices
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
starting_from_second_every_third_item = slice(1, -1, 3)

print(items[starting_from_second_every_third_item])

# 2. Slices in numpy
example_two_dim_array = np.array([[1, 2, 3], [4, 5, 6]])
print(example_two_dim_array[:1, ...])
print(example_two_dim_array[..., :1])
print(example_two_dim_array[:1, :2])