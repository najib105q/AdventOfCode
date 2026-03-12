def max_joltage_from_bank_12(bank: str, k: int = 12) -> int:
    stack = []
    n = len(bank)
    to_remove = n - k
    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    result_digits = stack[:k]
    return int("".join(result_digits))

def simulate_banks_part2(banks, k: int = 12) -> int:
    return sum(max_joltage_from_bank_12(bank, k) for bank in banks)

def total_output_joltage_part2(filepath: str, k: int = 12) -> int:
    with open(filepath, "r") as f:
        banks = [line.strip() for line in f if line.strip()]
    return simulate_banks_part2(banks, k)

# Example usage
example_banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

example_total = simulate_banks_part2(example_banks, k=12)
print(example_total)
print(total_output_joltage_part2("data/day03.txt", k=12))
