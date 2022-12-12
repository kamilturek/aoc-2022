import sys

ROUND_SCORES = {
    ("A", "X"): 3 + 1,
    ("A", "Y"): 6 + 2,
    ("A", "Z"): 0 + 3,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 6 + 1,
    ("C", "Y"): 0 + 2,
    ("C", "Z"): 3 + 3,
}


def solve(input):
    """
    >>> solve(open('input0.txt'))
    15
    >>> solve(open('input1.txt'))
    12794
    """
    return sum(
        ROUND_SCORES[(op_shape, my_shape)]
        for op_shape, my_shape in [round.strip().split(" ") for round in input]
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
