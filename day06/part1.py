import io
import sys


def solve(input):
    """
    >>> from io import StringIO
    >>> solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    7
    >>> solve('bvwbjplbgvbhsrlpgdmjqwftvncz')
    5
    >>> solve('nppdvjthqldpwncqszvftbrmjlhg')
    6
    >>> solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    10
    >>> solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    11
    >>> solve(open('input0.txt'))
    1766
    """
    windowsize = 4

    if isinstance(input, io.IOBase):
        input = next(input)

    for start in range(len(input) - windowsize):
        end = start + windowsize
        if len(set(input[start:end])) == windowsize:
            return end


if __name__ == "__main__":
    print(solve(sys.stdin))
