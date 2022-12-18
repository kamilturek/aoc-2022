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
    1
    >>> solve(open('input1.txt'))
    2607
    >>> solve(open('input2.txt'))
    36
    """
    knots = [Point(x=0, y=0) for i in range(0, 10)]
    head, tail = knots[0], knots[-1]
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

            for i, follower in enumerate(knots[1:], 1):
                followed = knots[i - 1]

                if followed.xdist(follower) == 2 and followed.ydist(follower) == 2:
                    followed.xpull(follower)
                    followed.ypull(follower)
                elif followed.xdist(follower) == 2:
                    followed.xpull(follower)
                    follower.y = followed.y
                elif followed.ydist(follower) == 2:
                    followed.ypull(follower)
                    follower.x = followed.x

            visited.add(astuple(tail))

    return len(visited)


if __name__ == "__main__":
    print(solve(sys.stdin))
