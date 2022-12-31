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


def find_shortest_distance(graph, start, end):
    """Dijkstra's Algorithm"""

    pq = []
    visited = set()
    costs = defaultdict(lambda: float("inf"))

    costs[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        for neighbour in graph[node]:
            if neighbour in visited:
                continue

            cost = costs[node] + 1
            if cost < costs[neighbour]:
                costs[neighbour] = cost
                heapq.heappush(pq, (cost, neighbour))

    return costs[end]


def solve(input):
    """
    >>> solve(open('input0.txt'))
    29
    >>> solve(open('input1.txt'))
    402
    """

    # Building graph and start & end
    graph = defaultdict(list)

    matrix = input.read().strip().splitlines()
    dim_y, dim_x = len(matrix), len(matrix[0])

    starts = []
    end = None

    for y, row in enumerate(matrix):
        for x, elem in enumerate(row):
            if elem == "S" or elem == "a":
                starts.append((y, x))
            if elem == "E":
                end = y, x

            neighbours = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
            neighbours = [
                (neighbour_y, neighbour_x)
                for neighbour_y, neighbour_x in neighbours
                if neighbour_y >= 0
                and neighbour_x >= 0
                and neighbour_y < dim_y
                and neighbour_x < dim_x
            ]

            for neighbour in neighbours:
                current_elevation = get_elevation(matrix, y, x)
                neighbour_elevation = get_elevation(matrix, *neighbour)
                if neighbour_elevation <= current_elevation + 1:
                    graph[y, x].append(neighbour)

    return min(find_shortest_distance(graph, start, end) for start in starts)


if __name__ == "__main__":
    print(solve(sys.stdin))
