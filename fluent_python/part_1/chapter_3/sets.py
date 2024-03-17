from unicodedata import name

haystack = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
needles = {2, 4, 6}
print(len(haystack & needles))

sign_chars = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(sign_chars)

some_dict = {'a': 1, 'b': 2, 'c': 3}
some_set = {'a', 'd', 'e'}
print(some_dict.keys() & some_set)