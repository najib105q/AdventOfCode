from typing import List, Tuple, Dict

def parse_input(lines: List[str]) -> Tuple[Dict[int, List[str]], List[Tuple[int, int, List[int]]]]:
    shapes: Dict[int, List[str]] = {}
    regions: List[Tuple[int, int, List[int]]] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if ":" in line and line.split(":")[0].isdigit():
            idx = int(line.split(":")[0])
            i += 1
            shape_lines = []
            while i < len(lines) and lines[i] and ":" not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            shapes[idx] = shape_lines
        else:
            break
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if "x" in line and ":" in line:
            size, counts = line.split(":")
            w, h = map(int, size.split("x"))
            quantities = list(map(int, counts.strip().split()))
            regions.append((w, h, quantities))
        i += 1
    return shapes, regions

def shape_area(shape: List[str]) -> int:
    return sum(row.count("#") for row in shape)

def shape_dims(shape: List[str]) -> Tuple[int,int]:
    return len(shape), len(shape[0])

def can_fit_region(width: int, height: int, quantities: List[int], shapes: Dict[int, List[str]]) -> bool:
    total_area = 0
    for idx, qty in enumerate(quantities):
        if qty == 0:
            continue
        area = shape_area(shapes[idx])
        h, w = shape_dims(shapes[idx])
        if h > height and w > width:
            return False
        total_area += qty * area
    return total_area <= width * height

def simulate_regions(lines: List[str]) -> int:
    shapes, regions = parse_input(lines)
    count = 0
    for w, h, quantities in regions:
        if can_fit_region(w, h, quantities, shapes):
            count += 1
    return count

def count_regions(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return simulate_regions(lines)

example_input = [
"0:",
"###",
"##.",
"##.",
"",
"1:",
"###",
"##.",
".##",
"",
"2:",
".##",
"###",
"##.",
"",
"3:",
"##.",
"###",
"##.",
"",
"4:",
"###",
"#..",
"###",
"",
"5:",
"###",
".#.",
"###",
"",
"4x4: 0 0 0 0 2 0",
"12x5: 1 0 1 0 2 2",
"12x5: 1 0 1 0 3 2"
]

print(simulate_regions(example_input))
print(count_regions("data/day12.txt"))
