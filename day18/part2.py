import sys
from collections import deque


def get_neighbours(cube):
    x, y, z = cube
    return (
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    )


def solve(input):
    """
    >>> solve(open('input0.txt'))
    58
    >>> solve(open('input1.txt'))
    2508
    """
    cubes = {tuple(map(int, line.split(","))) for line in input}

    min_coord = min(min(cube) for cube in cubes) - 1
    max_coord = max(max(cube) for cube in cubes) + 1

    queue = deque([(min_coord, min_coord, min_coord)])
    visited = set()
    touched = 0

    while len(queue) > 0:
        current = queue.popleft()
        if current in visited:
            continue

        visited.add(current)

        for n in get_neighbours(current):
            if any(coord > max_coord or coord < min_coord for coord in n):
                continue

            if n in cubes:
                touched += 1
            else:
                queue.append(n)

    return touched


if __name__ == "__main__":
    print(solve(sys.stdin))
