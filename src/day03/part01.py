def max_joltage_from_bank(bank: str) -> int:
    max_val = 0
    n = len(bank)
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])
            if val > max_val:
                max_val = val
    return max_val


def simulate_banks(banks):
    total = sum(max_joltage_from_bank(bank) for bank in banks)
    return total


def total_output_joltage(filepath: str) -> int:
    with open(filepath, "r") as f:
        banks = [line.strip() for line in f if line.strip()]
    return simulate_banks(banks)


# Example usage
example_banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

example_total = simulate_banks(example_banks)
print(example_total)
print(total_output_joltage("data/day03.txt"))
