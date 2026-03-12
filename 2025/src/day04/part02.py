from typing import List

def parse_grid(filepath: str) -> List[List[str]]:
    with open(filepath, "r") as f:
        return [list(line.strip()) for line in f if line.strip()]

def count_neighbors(grid: List[List[str]], r: int, c: int) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                count += 1
    return count

def remove_accessible(grid: List[List[str]]) -> int:
    total_removed = 0
    while True:
        to_remove = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "@":
                    if count_neighbors(grid, r, c) < 4:
                        to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = "."
        total_removed += len(to_remove)
    return total_removed

def count_total_removed(filepath: str) -> int:
    grid = parse_grid(filepath)
    return remove_accessible(grid)

example_grid = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@."
]

parsed = [list(row) for row in example_grid]
print(remove_accessible(parsed))
print(count_total_removed("data/day04.txt"))
