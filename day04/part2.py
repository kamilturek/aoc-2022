import sys


def is_intersection(one, two):
    lone, rone, ltwo, rtwo = *map(int, one.split("-")), *map(int, two.split("-"))
    return (
        (lone <= ltwo <= rone)
        or (lone <= rtwo <= rone)
        or (ltwo <= lone <= rtwo)
        or (ltwo <= rone <= rtwo)
    )


def solve(input):
    """
    >>> solve(open('input0.txt'))
    4
    >>> solve(open('input1.txt'))
    903
    """
    return sum(is_intersection(*pair.split(",")) for pair in input)


if __name__ == "__main__":
    print(solve(sys.stdin))
