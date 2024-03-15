import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, item):
        self.data[str(key)] = item


my_dict = StrKeyDict()
my_dict[1] = 'x'
my_dict['2'] = 'y'
print(my_dict['1'])
print(my_dict[2])
