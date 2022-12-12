import sys

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSE = "X"
DRAW = "Y"
WIN = "Z"

SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
    LOSE: 0,
    DRAW: 3,
    WIN: 6,
}

ROUND_SCORES = {
    (ROCK, LOSE): SCORES[SCISSORS] + SCORES[LOSE],
    (ROCK, DRAW): SCORES[ROCK] + SCORES[DRAW],
    (ROCK, WIN): SCORES[PAPER] + SCORES[WIN],
    (PAPER, LOSE): SCORES[ROCK] + SCORES[LOSE],
    (PAPER, DRAW): SCORES[PAPER] + SCORES[DRAW],
    (PAPER, WIN): SCORES[SCISSORS] + SCORES[WIN],
    (SCISSORS, LOSE): SCORES[PAPER] + SCORES[LOSE],
    (SCISSORS, DRAW): SCORES[SCISSORS] + SCORES[DRAW],
    (SCISSORS, WIN): SCORES[ROCK] + SCORES[WIN],
}


def solve(input):
    """
    >>> solve(open('input0.txt'))
    12
    >>> solve(open('input1.txt'))
    14979
    """
    return sum(
        ROUND_SCORES[(op_shape, my_shape)]
        for op_shape, my_shape in [round.strip().split(" ") for round in input]
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
