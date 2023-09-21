import sys


def get_cube_sides(x, y, z):
    return (
        ((x, x + 1), y, z),
        ((x - 1, x), y, z),
        (x, (y, y + 1), z),
        (x, (y - 1, y), z),
        (x, y, (z, z + 1)),
        (x, y, (z - 1, z)),
    )


def solve(input):
    """
    >>> solve(open('input0.txt'))
    64
    >>> solve(open('input1.txt'))
    4364
    """
    exposed_sides = set()

    for cube in input:
        x, y, z = map(int, cube.split(","))
        exposed_sides ^= set(get_cube_sides(x, y, z))

    return len(exposed_sides)


if __name__ == "__main__":
    print(solve(sys.stdin))
