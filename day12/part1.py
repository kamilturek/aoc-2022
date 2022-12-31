import sys
import heapq
from collections import defaultdict


ELEVATION_MAPPING = {
    "S": "a",
    "E": "z",
}


def get_elevation(matrix, y, x):
    elevation = matrix[y][x]
    return ord(ELEVATION_MAPPING.get(elevation, elevation))


def find_shortest_distance(matrix, start, end):
    dim_y, dim_x = len(matrix), len(matrix[0])
    pq = []
    visited = set()

    heapq.heappush(pq, (0, start))

    while pq:
        cost, curr = heapq.heappop(pq)
        cy, cx = curr

        if curr == end:
            return cost

        if curr in visited:
            continue

        visited.add(curr)

        for neighbour in [(cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)]:
            if neighbour in visited:
                continue

            ny, nx = neighbour
            if nx < 0 or ny < 0 or nx >= dim_x or ny >= dim_y:
                continue

            celev = get_elevation(matrix, cy, cx)
            nelev = get_elevation(matrix, ny, nx)
            if nelev > celev + 1:
                continue

            heapq.heappush(pq, (cost + 1, neighbour))

    return float("inf")


def solve(input):
    """
    >>> solve(open('input0.txt'))
    31
    >>> solve(open('input1.txt'))
    412
    """
    matrix = input.read().strip().splitlines()
    start = None
    end = None

    for y, row in enumerate(matrix):
        for x, elem in enumerate(row):
            if elem == "S":
                start = y, x
            if elem == "E":
                end = y, x

    return find_shortest_distance(matrix, start, end)


if __name__ == "__main__":
    print(solve(sys.stdin))
