import sys
from itertools import pairwise


def move_towards(start, end):
    start_x, start_y = start
    end_x, end_y = end

    if start_x > end_x:
        return start_x - 1, start_y
    if start_x < end_x:
        return start_x + 1, start_y
    if start_y > end_y:
        return start_x, start_y - 1
    if start_y < end_y:
        return start_x, start_y + 1


def solve(input):
    """
    >>> solve(open('input0.txt'))
    93
    >>> solve(open('input1.txt'))
    24943
    """
    blocked = set()

    for path in input:
        lines = map(
            lambda point: tuple(map(int, point.strip().split(","))), path.split("->")
        )
        for start, end in pairwise(lines):
            curr = start
            while curr != end:
                blocked.add(curr)
                curr = move_towards(curr, end)
            blocked.add(end)

    floor = max(y for _, y in blocked) + 2
    sand_count = 0

    while True:
        sand_x, sand_y = (500, 0)
        sand_count += 1
        is_blocked = lambda pos: pos in blocked or pos[1] == floor

        while True:

            if not is_blocked((sand_x, sand_y + 1)):
                sand_y += 1
            elif not is_blocked((sand_x - 1, sand_y + 1)):
                sand_x -= 1
                sand_y += 1
            elif not is_blocked((sand_x + 1, sand_y + 1)):
                sand_x += 1
                sand_y += 1
            elif (sand_x, sand_y) == (500, 0):
                return sand_count
            else:
                blocked.add((sand_x, sand_y))
                break


if __name__ == "__main__":
    print(solve(sys.stdin))
