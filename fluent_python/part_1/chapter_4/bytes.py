import array


some_bytes = bytes('kawę', encoding='utf-8')
print(some_bytes)
print(some_bytes[0])
print(some_bytes[:1])

some_numbers = array.array('h', [-2, -1, 0, 1, 2])
some_numbers_as_octets = bytes(some_numbers)
print(some_numbers_as_octets)