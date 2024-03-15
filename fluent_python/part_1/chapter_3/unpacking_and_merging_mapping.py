dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'd': 5}
print({**dict1, **dict2})

print(dict1 | dict2)
dict1 |= dict2
print(dict1)