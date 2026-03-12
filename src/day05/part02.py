from typing import List, Tuple

def parse_ranges(filepath: str) -> List[Tuple[int,int]]:
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f]
    split_index = lines.index("")
    return [tuple(map(int, line.split("-"))) for line in lines[:split_index]]

def merge_ranges(ranges: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    ranges.sort()
    merged = []
    for lo, hi in ranges:
        if not merged or lo > merged[-1][1] + 1:
            merged.append((lo, hi))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
    return merged

def count_all_fresh_ranges(ranges: List[Tuple[int,int]]) -> int:
    merged = merge_ranges(ranges)
    return sum(hi - lo + 1 for lo, hi in merged)

def count_all_fresh(filepath: str) -> int:
    ranges = parse_ranges(filepath)
    return count_all_fresh_ranges(ranges)

example_ranges = [(3,5),(10,14),(16,20),(12,18)]
print(count_all_fresh_ranges(example_ranges))
print(count_all_fresh("data/day05.txt"))
