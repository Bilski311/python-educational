import json

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, coordinates=(35.689722, 139.691667))
print(tokyo.population)
print(json.dumps(tokyo._asdict()))