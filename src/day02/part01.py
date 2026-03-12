def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def simulate_ranges(ranges):
    total = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

def count_invalid_ids(filepath: str) -> int:
    with open(filepath, "r") as f:
        input_line = f.read().strip()
    ranges = [r for r in input_line.split(",") if r]
    return simulate_ranges(ranges)

# Example usage
example_input = [
    "11-22","95-115","998-1012","1188511880-1188511890",
    "222220-222224","1698522-1698528","446443-446449",
    "38593856-38593862","565653-565659","824824821-824824827",
    "2121212118-2121212124"
]

print(simulate_ranges(example_input))
print(count_invalid_ids("data/day02.txt"))
