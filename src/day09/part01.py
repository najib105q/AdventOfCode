from typing import List, Tuple

def parse_input(lines: List[str]) -> List[Tuple[int,int]]:
    return [tuple(map(int, line.split(","))) for line in lines]

def compute_pairs(coords: List[Tuple[int,int]]) -> List[int]:
    areas = []
    n = len(coords)
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            areas.append((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
    return areas

def largest_rectangle(lines: List[str]) -> int:
    coords = parse_input(lines)
    areas = compute_pairs(coords)
    return max(areas) if areas else 0

def simulate_grid(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return largest_rectangle(lines)

example_input = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3"
]

print(largest_rectangle(example_input))
print(simulate_grid("data/day09.txt"))
