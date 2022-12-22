import math
import re
import sys
from collections import deque
from dataclasses import dataclass
from operator import add, mul
from typing import Callable, Self

OPERATION_PATTERN = re.compile(
    r"Operation: new = old (?P<operator>\+|\*) (?P<arg>old|\d+)"
)


def get_func(operator, arg):
    match (operator, arg):
        case (_, "old"):
            return lambda x: x * x
        case ("*", arg):
            return lambda x: x * int(arg)
        case ("+", arg):
            return lambda x: x + int(arg)


@dataclass
class Monkey:
    items: deque[int]
    modulo: int
    func: Callable[[int], int]
    target_true_index: int
    target_false_index: int

    inspections_done: int = 0

    @classmethod
    def from_text(cls, text: str) -> Self:
        properties = [line.strip() for line in text.splitlines()]

        items = re.findall(r"\d+", properties[1])
        operator, arg = OPERATION_PATTERN.match(properties[2]).groups()
        func = get_func(operator, arg)
        modulo = re.search(r"\d+", properties[3]).group()
        target_true_index = re.search(r"\d+", properties[4]).group()
        target_false_index = re.search(r"\d+", properties[5]).group()

        return Monkey(
            items=deque(map(int, items)),
            func=func,
            modulo=int(modulo),
            target_true_index=int(target_true_index),
            target_false_index=int(target_false_index),
        )


def solve(input):
    """
    >>> solve(open('input0.txt'))
    10605
    >>> solve(open('input1.txt'))
    55930
    """
    input = input.read().split("\n\n")

    monkeys = [Monkey.from_text(section) for section in input]

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items):
                worry_level = monkey.items.popleft()
                worry_level = monkey.func(worry_level)
                worry_level = math.floor(worry_level / 3)
                target_index = (
                    monkey.target_true_index
                    if worry_level % monkey.modulo == 0
                    else monkey.target_false_index
                )
                monkeys[target_index].items.append(worry_level)
                monkey.inspections_done += 1

    return mul(*sorted([monkey.inspections_done for monkey in monkeys])[-2:])


if __name__ == "__main__":
    print(solve(sys.stdin))
