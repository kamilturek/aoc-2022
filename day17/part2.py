import itertools
import sys
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Vector:
    x: int
    y: int


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def move(self, vector: Vector) -> "Point":
        return self.__class__(
            x=self.x + vector.x,
            y=self.y + vector.y,
        )


@dataclass
class Rock:
    points: list[Point]

    def __iter__(self) -> Iterator[Point]:
        return iter(self.points)

    def move(self, vector: Vector) -> "Rock":
        return self.__class__([point.move(vector) for point in self.points])


def get_state(stuck: set[Point]) -> list[int]:
    state = [-20] * 7

    for p in stuck:
        state[p.x] = max(state[p.x], p.y)

    top = max(state)

    return [top - y for y in state]


def solve(input):
    """
    >>> solve(open('input0.txt'))
    1514285714288
    >>> solve(open('input1.txt'))
    1584927536247
    """
    rocks = itertools.cycle(
        (
            # -
            (Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)),
            # +
            (Point(1, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 2)),
            # _|
            (Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)),
            # |
            (Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)),
            # []
            (Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)),
        )
    )

    height = 0
    stuck = set()

    rock = Rock(list(next(rocks)))
    rock = rock.move(Vector(2, 3))
    rock_index = 0

    seen = {}
    cycle_height = 0

    gases = input.read()

    limit = 1000000000000

    for gas_index, gas in enumerate(itertools.cycle(gases)):
        if rock_index == limit:
            return height + cycle_height

        if gas == ">":
            moved_rock = rock.move(Vector(1, 0))
        else:
            moved_rock = rock.move(Vector(-1, 0))

        if (
            not stuck & set(moved_rock)
            and all(p.x >= 0 for p in moved_rock)
            and all(p.x <= 6 for p in moved_rock)
        ):
            rock = moved_rock

        moved_rock = rock.move(Vector(0, -1))

        if any(p.y == -1 for p in moved_rock) or stuck & set(moved_rock):
            for p in rock:
                stuck.add(p)
            height = max(max(p.y for p in rock) + 1, height)
            rock = Rock(list(next(rocks)))
            rock = rock.move(Vector(2, height + 3))
            rock_index += 1

            key = (rock_index % 5, gas_index % len(gases), tuple(get_state(stuck)))
            if key in seen:
                prev_rock_index, prev_height = seen[key]
                offset = rock_index - prev_rock_index
                rem = limit - rock_index
                rep = rem // offset
                cycle_height += rep * (height - prev_height)
                rock_index += offset * rep
                seen = {}
            seen[key] = (rock_index, height)
            continue

        rock = moved_rock


if __name__ == "__main__":
    print(solve(sys.stdin))
