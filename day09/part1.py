import sys
from dataclasses import astuple, dataclass


@dataclass
class Point:
    x: int
    y: int

    def xdist(self, other):
        return abs(self.x - other.x)

    def ydist(self, other):
        return abs(self.y - other.y)

    def xpull(self, other):
        if self.x < other.x:
            other.x -= 1
        else:
            other.x += 1

    def ypull(self, other):
        if self.y < other.y:
            other.y -= 1
        else:
            other.y += 1


def solve(input):
    """
    >>> solve(open('input0.txt'))
    13
    >>> solve(open('input1.txt'))
    6376
    """
    head = Point(x=0, y=0)
    tail = Point(x=0, y=0)
    visited = {astuple(tail)}

    for line in input:
        direction, step = line.strip().split(" ")

        for _ in range(int(step)):
            match direction:
                case "L":
                    head.x -= 1
                case "R":
                    head.x += 1
                case "U":
                    head.y += 1
                case "D":
                    head.y -= 1

            if head.xdist(tail) == 2:
                head.xpull(tail)
                tail.y = head.y
            elif head.ydist(tail) == 2:
                head.ypull(tail)
                tail.x = head.x

            visited.add(astuple(tail))

    return len(visited)


if __name__ == "__main__":
    print(solve(sys.stdin))
