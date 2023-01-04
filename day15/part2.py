"""
Benchmarks:
    * CPython 3.11.0
        $ python --version
        Python 3.11.0
        $ time cat input1.txt | python part2.py 4000000 4000000
        12051287042458
        cat input1.txt  0.00s user 0.00s system 83% cpu 0.008 total
        python part2.py 4000000 4000000  28.94s user 0.07s system 99% cpu 29.048 total
    
    * PyPy 3.9.12:
        $ python --version
        Python 3.9.12 (05fbe3aa5b0845e6c37239768aa455451aa5faba, Mar 29 2022, 09:54:47)
        [PyPy 7.3.9 with GCC Apple LLVM 13.0.0 (clang-1300.0.29.30)]
        $ time cat input1.txt | python part2.py 4000000 4000000
        12051287042458
        cat input1.txt  0.00s user 0.00s system 84% cpu 0.008 total
        python part2.py 4000000 4000000  1.84s user 0.03s system 98% cpu 1.909 total
"""

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


def solve(input, xmax, ymax):
    """
    >>> solve(open('input0.txt'), xmax=20, ymax=20)
    56000011
    >>> solve(open('input1.txt'), xmax=4000000, ymax=4000000)
    12051287042458
    """
    sensors = []
    beacons = set()

    for line in input:
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        spos, bpos = Point(sx, sy), Point(bx, by)
        sensors.append(Sensor(pos=spos, range=spos.distance_to(bpos)))
        beacons.add(bpos)

    for sensor in sensors:
        max_x = sensor.pos.x + sensor.range + 1
        min_x = sensor.pos.x - sensor.range - 1
        max_y = sensor.pos.y + sensor.range + 1
        min_y = sensor.pos.y - sensor.range - 1

        for d in range(sensor.range):
            for x, y in (
                (sensor.pos.x + d, min_y + d),
                (sensor.pos.x - d, max_y - d),
                (max_x - d, sensor.pos.y + d),
                (min_x + d, sensor.pos.y - d),
            ):
                if not (0 <= x <= xmax and 0 <= y < ymax):
                    continue

                point = Point(x, y)

                if point in beacons:
                    continue

                for sen in sensors:
                    if sen.covers(point):
                        break
                else:
                    return x * 4000000 + y


if __name__ == "__main__":
    print(solve(sys.stdin, int(sys.argv[1]), int(sys.argv[2])))
