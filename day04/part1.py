import sys


def is_subset(one, two):
    lone, rone, ltwo, rtwo = *map(int, one.split("-")), *map(int, two.split("-"))
    return (lone <= ltwo <= rtwo <= rone) or (ltwo <= lone <= rone <= rtwo)


def solve(input):
    """
    >>> solve(open('input0.txt'))
    2
    >>> solve(open('input1.txt'))
    530
    """
    return sum(is_subset(*pair.split(",")) for pair in input)


if __name__ == "__main__":
    print(solve(sys.stdin))
