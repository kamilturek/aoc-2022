import sys

NOOP = "noop"
ADDX = "addx"

INSTRUCTION_CYCLES = {
    NOOP: 1,
    ADDX: 2,
}


def solve(input):
    """
    >>> print(solve(open('input0.txt')))
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....
    >>> print(solve(open('input1.txt')))
    ####..##...##..#..#.####.###..####..##..
    #....#..#.#..#.#..#....#.#..#.#....#..#.
    ###..#....#....#..#...#..#..#.###..#....
    #....#.##.#....#..#..#...###..#....#....
    #....#..#.#..#.#..#.#....#.#..#....#..#.
    #.....###..##...##..####.#..#.####..##..
    """
    x = 1
    cycle = 1
    crt = 0
    image = ""

    for line in input:
        instruction, *args = line.strip().split(" ")
        cycles = INSTRUCTION_CYCLES[instruction]

        for _ in range(cycles):
            if x - 1 <= crt <= x + 1:
                image += "#"
            else:
                image += "."

            cycle += 1
            crt += 1

            if cycle % 40 == 1:
                crt = 0
                image += "\n"

        if instruction == ADDX:
            x += int(args[0])

    return image.strip()


if __name__ == "__main__":
    print(solve(sys.stdin))
