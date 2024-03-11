def fixed(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False


tuple_containing_tuple = ('something', 'something', (1, 2))
tuple_containing_list = ('something', 'something', [1, 2])

print(fixed(tuple_containing_tuple))
print(fixed(tuple_containing_list))
