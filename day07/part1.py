import string
import sys
from collections import Counter
from itertools import accumulate

CD = "$ cd "


def solve(input):
    """
    >>> solve(open('input0.txt'))
    95437
    >>> solve(open('input1.txt'))
    1307902
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

    return sum(size for size in dirsizes.values() if size <= 100000)


if __name__ == "__main__":
    print(solve(sys.stdin))
