from typing import List, Tuple

def parse_input(lines: List[str]) -> List[Tuple[int,int]]:
    return [tuple(map(int, line.split(","))) for line in lines]

def compute_pairs(coords: List[Tuple[int,int]]) -> List[int]:
    n = len(coords)
    vertical = []
    for i in range(n):
        nxt = coords[(i + 1) % n]
        vertical.append(coords[i][0] == nxt[0])

    areas = []
    for i in range(n):
        for j in range(i + 1, n):
            if vertical[i] == vertical[j]:
                lowX = min(coords[i][0], coords[j][0])
                highX = max(coords[i][0], coords[j][0])
                lowY = min(coords[i][1], coords[j][1])
                highY = max(coords[i][1], coords[j][1])

                ok = True
                for k in range(n - 1):
                    a = coords[k]
                    b = coords[k + 1]
                    if vertical[k]:
                        if (lowX < a[0] < highX and
                            max(a[1], b[1]) > lowY and
                            min(a[1], b[1]) < highY):
                            ok = False
                            break
                    else:
                        if (lowY < a[1] < highY and
                            max(a[0], b[0]) > lowX and
                            min(a[0], b[0]) < highX):
                            ok = False
                            break

                if ok:
                    dx = highX - lowX + 1
                    dy = highY - lowY + 1
                    areas.append(dx * dy)
    return areas

def largest_rectangle_colored(lines: List[str]) -> int:
    coords = parse_input(lines)
    areas = compute_pairs(coords)
    return max(areas) if areas else 0

def simulate_grid_colored(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return largest_rectangle_colored(lines)

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

print(largest_rectangle_colored(example_input))
print(simulate_grid_colored("data/day09.txt"))
