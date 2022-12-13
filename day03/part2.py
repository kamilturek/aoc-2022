import functools
import string
import sys

PRIORITIES = {
    letter: priority for priority, letter in enumerate(string.ascii_letters, 1)
}


def group_misarrangement(rucksacks: list[str]) -> int:
    common = set.intersection(*[set(rucksack) for rucksack in rucksacks])
    return PRIORITIES[common.pop()]


def solve(input):
    """
    >>> solve(open('input0.txt'))
    70
    >>> solve(open('input1.txt'))
    2633
    """
    rucksacks = input.read().strip().splitlines()
    return sum(
        group_misarrangement(rucksacks[i : i + 3]) for i in range(0, len(rucksacks), 3)
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
