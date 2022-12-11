import sys


def solve(input):
    """
    >>> solve(open('input0.txt'))
    24000
    >>> solve(open('input1.txt'))
    67658
    """
    return max([sum(map(int, elf.splitlines())) for elf in input.read().split("\n\n")])


if __name__ == "__main__":
    print(solve(sys.stdin))
