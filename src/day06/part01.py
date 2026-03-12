from typing import List

def simulate_worksheet(lines: List[str]) -> int:
    width = max(len(line) for line in lines)
    col = 0
    blocks = []
    while col < width:
        if all(line[col] == " " for line in lines):
            col += 1
            continue
        start = col
        while col < width and not all(line[col] == " " for line in lines):
            col += 1
        blocks.append((start, col))
    total = 0
    for start, end in blocks:
        entries = [line[start:end].strip() for line in lines if line[start:end].strip()]
        op = entries[-1]
        nums = [int(x) for x in entries[:-1]]
        if op == "+":
            total += sum(nums)
        elif op == "*":
            result = 1
            for n in nums:
                result *= n
            total += result
    return total

def count_total(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return simulate_worksheet(lines)

example_input = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "
]

print(simulate_worksheet(example_input))
print(count_total("data/day06.txt"))
