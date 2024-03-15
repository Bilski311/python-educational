import types

some_dict = {1: 'A'}
proxy = types.MappingProxyType(some_dict)
print(proxy)
try:
    proxy[2] = 'B'
except TypeError:
    print('Unable to change proxy.')

print(proxy)
some_dict[2] = 'B'
print(proxy)