import functools
import re
import sys
from collections import deque

PATTERN = re.compile(
    r"^Valve (?P<name>\w{2}) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<tunnels>.*)$"
)


def solve(input):
    """
    >>> solve(open('input0.txt'))
    1651
    >>> solve(open('input1.txt'))
    1580
    """
    tunnels = {}
    flows = {}
    costs = {}

    for line in input:
        match = PATTERN.match(line)
        valve = match.group("name")
        tunnels[valve] = [
            tunnel.strip() for tunnel in match.group("tunnels").split(",")
        ]
        flows[valve] = int(match.group("rate"))

    # Reduce the graph by removing the nodes with rate of 0.
    # Calculate distances between every pair of relevant valves.
    for valve in tunnels:
        # AA has to stay as we'll start from it.
        if valve != "AA" and flows[valve] == 0:
            continue

        visited = set()
        q = deque([(0, valve)])
        costs[valve] = {}

        while q:
            distance, current = q.popleft()
            if current in visited:
                continue

            visited.add(current)

            for neighbour in tunnels[current]:
                if neighbour in visited:
                    continue

                # Since all the edges have the same weight (1),
                # when we reach the node, we can be sure it's the closest path.
                # It's BFS after all.
                cost = distance + 1

                # Save node only if the valve is relevant.
                if flows[neighbour] > 0:
                    costs[valve][neighbour] = cost

                q.append((cost, neighbour))

    valve_indexes = {valve: i for i, valve in enumerate(costs)}

    def open_valve(valve, state):
        return state | (1 << valve_indexes[valve])

    def is_valve_open(valve, state):
        return bool(state & (1 << valve_indexes[valve]))

    @functools.cache
    def dfs(current, time_left, state):
        curr_flow = time_left * flows[current]
        state = open_valve(current, state)

        max_flow = 0
        for destination in costs[current]:
            if flows[destination] == 0:
                continue

            if is_valve_open(destination, state):
                continue

            cost = costs[current][destination] + 1
            if time_left - cost <= 0:
                continue

            max_flow = max(max_flow, dfs(destination, time_left - cost, state))

        return curr_flow + max_flow

    valves_opened = 0
    valves_opened = open_valve("AA", valves_opened)

    return dfs("AA", 30, valves_opened)


if __name__ == "__main__":
    print(solve(sys.stdin))
