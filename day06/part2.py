import io
import sys


def solve(input):
    """
    >>> from io import StringIO
    >>> solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    19
    >>> solve('bvwbjplbgvbhsrlpgdmjqwftvncz')
    23
    >>> solve('nppdvjthqldpwncqszvftbrmjlhg')
    23
    >>> solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    29
    >>> solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    26
    >>> solve(open('input0.txt'))
    2383
    """
    windowsize = 14

    if isinstance(input, io.IOBase):
        input = next(input)

    for start in range(len(input) - windowsize):
        end = start + windowsize
        if len(set(input[start:end])) == windowsize:
            return end


if __name__ == "__main__":
    print(solve(sys.stdin))
