import sys


def get_row(matrix, index):
    return matrix[index]


def get_col(matrix, index):
    return [row[index] for row in matrix]


def is_visible(tree, neighbours):
    return all(tree > neighbour for neighbour in neighbours)


def solve(input):
    """
    >>> solve(open('input0.txt'))
    21
    >>> solve(open('input1.txt'))
    1851
    """
    matrix = input.read().splitlines()
    width = len(get_row(matrix, 0))
    height = len(get_col(matrix, 0))
    visible = 2 * width + 2 * height - 4

    for row_index in range(1, width - 1):
        for col_index in range(1, height - 1):
            tree = matrix[row_index][col_index]
            row = get_row(matrix, row_index)
            col = get_col(matrix, col_index)

            left = row[:col_index]
            top = col[:row_index]
            right = row[col_index + 1 :]
            bottom = col[row_index + 1 :]

            if (
                is_visible(tree, left)
                or is_visible(tree, top)
                or is_visible(tree, right)
                or is_visible(tree, bottom)
            ):
                visible += 1

    return visible


if __name__ == "__main__":
    print(solve(sys.stdin))
