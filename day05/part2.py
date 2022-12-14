import re
import sys


def solve(input):
    """
    >>> solve(open('input0.txt'))
    'MCD'
    >>> solve(open('input1.txt'))
    'QLFQDBBHM'
    """
    crates, procedures = input.read().split("\n\n")
    *crates, labels = crates.splitlines()
    procedures = procedures.splitlines()

    stacks_count = int(labels[-2])
    stacks = [[] for _ in range(stacks_count)]

    for create_row in crates:
        for i, crate in enumerate(create_row[1::4]):
            if not crate.isspace():
                stacks[i].insert(0, crate)

    for procedure in procedures:
        match = re.match(
            r"^move (?P<count>\d+) from (?P<src>\d+) to (?P<dst>\d+)$", procedure
        )
        count = int(match.group("count"))
        src = int(match.group("src"))
        dst = int(match.group("dst"))

        stacks[dst - 1].extend(stacks[src - 1][-count:])
        del stacks[src - 1][-count:]

    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    print(solve(sys.stdin))
