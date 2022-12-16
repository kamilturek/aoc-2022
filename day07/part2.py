import string
import sys
from collections import Counter
from itertools import accumulate

CD = "$ cd "

TOTAL = 70000000
NEEDED = 30000000


def solve(input):
    """
    >>> solve(open('input0.txt'))
    24933642
    >>> solve(open('input1.txt'))
    7068748
    """
    path = []
    dirsizes = Counter()

    for line in input:
        line = line.strip()

        if line.startswith(CD):
            dirname = line[len(CD) :]
            if dirname == "/":
                path = ["/"]
            elif dirname == "..":
                path.pop()
            else:
                path.append(dirname)
        elif line.startswith(tuple(string.digits)):
            filesize = int(line.split(" ")[0])
            for partial in accumulate(path, lambda a, b: a + "/" + b):
                dirsizes[partial] += filesize

    rootsize = dirsizes["/"]
    freespace = TOTAL - rootsize

    return min(size for size in dirsizes.values() if freespace + size > NEEDED)


if __name__ == "__main__":
    print(solve(sys.stdin))
