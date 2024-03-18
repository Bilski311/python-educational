import json

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates hdi', defaults=['very high'])
tokyo = City('Tokyo', 'JP', 36.933, coordinates=(35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(json.dumps(tokyo._asdict()))