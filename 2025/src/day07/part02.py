from typing import List
from functools import lru_cache

def simulate_timelines(lines: List[str]) -> int:
    height = len(lines)
    width = max(len(line) for line in lines)
    grid = [list(line.ljust(width, '.')) for line in lines]

    start_row, start_col = None, None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break
    if start_row is None or start_col is None:
        raise ValueError("No start position 'S' found in input")

    @lru_cache(None)
    def count_paths(r: int, c: int) -> int:
        if not (0 <= r < height and 0 <= c < width):
            return 1
        ch = grid[r][c]
        if ch == '.':
            return count_paths(r+1, c)
        elif ch == '^':
            return count_paths(r+1, c-1) + count_paths(r+1, c+1)
        else:
            return count_paths(r+1, c)

    return count_paths(start_row+1, start_col)

def count_timelines(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return simulate_timelines(lines)

example_input = [
".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"..............."
]

print(simulate_timelines(example_input))
print(count_timelines("data/day07.txt"))
