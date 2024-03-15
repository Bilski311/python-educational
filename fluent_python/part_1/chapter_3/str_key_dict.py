class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

my_dict = StrKeyDict()
my_dict[1] = 'x'
my_dict['2'] = 'y'
print(my_dict[1])
print(my_dict[2])