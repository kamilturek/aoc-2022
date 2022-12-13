import string
import sys

PRIORITIES = {
    letter: priority for priority, letter in enumerate(string.ascii_letters, 1)
}


def rucksack_misarrangement(rucksack: str) -> int:
    half = len(rucksack) // 2
    first, second = set(rucksack[:half]), set(rucksack[half:])
    common = first & second
    return sum(PRIORITIES[letter] for letter in common)


def solve(input):
    """
    >>> solve(open('input0.txt'))
    157
    >>> solve(open('input1.txt'))
    7785
    """
    return sum(rucksack_misarrangement(line) for line in input)


if __name__ == "__main__":
    print(solve(sys.stdin))
