from typing import NamedTuple
from dataclasses import dataclass

@dataclass
class Coordinate:
    lat: float
    lon: float
    reference: str = 'WGS84'
    something = 'A'

coordinate = Coordinate(1, 2)
print(coordinate)
coordinate.lat = 2
coordinate.lon = 4
coordinate.reference = 'XD'
coordinate.something = 'B'
print(coordinate)