from typing import List
from collections import deque

def simulate_beams(lines: List[str]) -> int:
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

    queue = deque([(start_row+1, start_col)])
    splits = 0
    visited = set()

    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if not (0 <= r < height and 0 <= c < width):
            continue

        ch = grid[r][c]
        if ch == '.':
            queue.append((r+1, c))
        elif ch == '^':
            splits += 1
            if c-1 >= 0:
                queue.append((r+1, c-1))
            if c+1 < width:
                queue.append((r+1, c+1))
        else:
            queue.append((r+1, c))

    return splits

def count_splits(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return simulate_beams(lines)

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

print(simulate_beams(example_input))
print(count_splits("data/day07.txt"))
