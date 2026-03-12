from typing import List

def simulate_worksheet_vertically(lines: List[str]) -> int:
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
        numbers = []
        for c in range(end - 1, start - 1, -1):
            digits = [line[c] for line in lines[:-1]]
            num_str = "".join(d for d in digits if d.isdigit())
            if num_str:
                numbers.append(int(num_str))
        op = lines[-1][start:end].strip()
        if op == "+":
            total += sum(numbers)
        elif op == "*":
            result = 1
            for n in numbers:
                result *= n
            total += result
    return total

def count_total_vertically(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return simulate_worksheet_vertically(lines)

example_input = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "
]

print(simulate_worksheet_vertically(example_input))
print(count_total_vertically("data/day06.txt"))
