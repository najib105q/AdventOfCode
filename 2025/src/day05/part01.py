from typing import List, Tuple

def parse_database(filepath: str) -> Tuple[List[Tuple[int,int]], List[int]]:
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip() or line == "\n"]
    split_index = lines.index("")
    ranges = [tuple(map(int, line.split("-"))) for line in lines[:split_index]]
    ids = [int(line) for line in lines[split_index+1:]]
    return ranges, ids

def is_fresh(ranges: List[Tuple[int,int]], ingredient_id: int) -> bool:
    for lo, hi in ranges:
        if lo <= ingredient_id <= hi:
            return True
    return False

def count_fresh(filepath: str) -> int:
    ranges, ids = parse_database(filepath)
    return sum(1 for i in ids if is_fresh(ranges, i))

example_ranges = [(3,5),(10,14),(16,20),(12,18)]
example_ids = [1,5,8,11,17,32]
print(sum(1 for i in example_ids if is_fresh(example_ranges, i)))
print(count_fresh("data/day05.txt"))
