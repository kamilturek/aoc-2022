import sys


def get_row(matrix, index):
    return matrix[index]


def get_col(matrix, index):
    return [row[index] for row in matrix]


def get_viewing_distance(tree, neighbours):
    score = 0

    for neighbour in neighbours:
        score += 1
        if neighbour >= tree:
            break

    return score


def solve(input):
    """
    >>> solve(open('input0.txt'))
    8
    >>> solve(open('input1.txt'))
    574080
    """
    matrix = input.read().splitlines()
    width = len(get_row(matrix, 0))
    height = len(get_col(matrix, 0))
    best = 0

    for row_index in range(0, width):
        for col_index in range(0, height):
            tree = matrix[row_index][col_index]
            row = get_row(matrix, row_index)
            col = get_col(matrix, col_index)

            left = reversed(row[:col_index])
            top = reversed(col[:row_index])
            right = row[col_index + 1 :]
            bottom = col[row_index + 1 :]

            score = (
                get_viewing_distance(tree, left)
                * get_viewing_distance(tree, top)
                * get_viewing_distance(tree, right)
                * get_viewing_distance(tree, bottom)
            )
            best = max(best, score)

    return best


if __name__ == "__main__":
    print(solve(sys.stdin))
