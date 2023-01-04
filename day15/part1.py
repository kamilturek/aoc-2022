import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def distance_to(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass
class Sensor:
    pos: Point
    range: int

    def covers(self, point: Point) -> bool:
        return self.pos.distance_to(point) <= self.range


def solve(input, y):
    """
    >>> solve(open('input0.txt'), y=10)
    26
    >>> solve(open('input1.txt'), y=2000000)
    4725496
    """
    sensors = []
    beacons = set()

    for line in input:
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        spos, bpos = Point(sx, sy), Point(bx, by)
        sensors.append(Sensor(pos=spos, range=spos.distance_to(bpos)))
        beacons.add(bpos)

    min_x = min(sensor.pos.x - sensor.range for sensor in sensors)
    max_x = max(sensor.pos.x + sensor.range for sensor in sensors)

    covered = 0
    for x in range(min_x, max_x + 1):
        point = Point(x, y)
        if point in beacons:
            continue

        for sensor in sensors:
            if sensor.covers(point):
                covered += 1
                break

    return covered


if __name__ == "__main__":
    print(solve(sys.stdin, int(sys.argv[1])))
