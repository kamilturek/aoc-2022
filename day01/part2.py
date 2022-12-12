import sys


def solve(input):
    """
    >>> solve(open('input0.txt'))
    45000
    >>> solve(open('input1.txt'))
    200158
    """
    return sum(
        sorted(sum(map(int, elf.splitlines())) for elf in input.read().split("\n\n"))[
            -3:
        ]
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
