import sys

NOOP = "noop"
ADDX = "addx"

INSTRUCTION_CYCLES = {
    NOOP: 1,
    ADDX: 2,
}

CHECKPOINTS = [20, 60, 100, 140, 180, 220]


def solve(input):
    """
    >>> solve(open('input0.txt'))
    13140
    >>> solve(open('input1.txt'))
    17380
    """
    x = 1
    cycle = 1
    result = 0

    for line in input:
        instruction, *args = line.strip().split(" ")
        cycles = INSTRUCTION_CYCLES[instruction]

        for _ in range(cycles):
            if cycle in CHECKPOINTS:
                result += x * cycle
            cycle += 1

        if instruction == ADDX:
            x += int(args[0])

    return result


if __name__ == "__main__":
    print(solve(sys.stdin))
