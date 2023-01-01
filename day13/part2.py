import sys
import ast
from itertools import zip_longest
from functools import cmp_to_key


def force_list(val):
    return [val] if not isinstance(val, list) else val


def compare(left, right):
    """
    >>> compare(1, 2) > 0  # right order
    True
    >>> compare(2, 1) < 0  # wrong order
    True
    >>> compare(1, 1) == 0  # keep checking
    True
    """
    if isinstance(left, int) and isinstance(right, int):
        return right - left

    left = force_list(left)
    right = force_list(right)

    for lelem, relem in zip_longest(left, right):
        if lelem is None:
            return 1
        if relem is None:
            return -1
        if (diff := compare(lelem, relem)) != 0:
            return diff

    return 0


def solve(input):
    """
    >>> solve(open('input0.txt'))
    140
    >>> solve(open('input1.txt'))
    29025
    """
    packets = [
        ast.literal_eval(packet)
        for pair in input.read().strip().split("\n\n")
        for packet in pair.splitlines()
    ]

    divider1 = [[2]]
    divider2 = [[6]]

    packets.extend([divider1, divider2])
    packets.sort(key=cmp_to_key(compare), reverse=True)

    return (packets.index(divider1) + 1) * (packets.index(divider2) + 1)


if __name__ == "__main__":
    print(solve(sys.stdin))
