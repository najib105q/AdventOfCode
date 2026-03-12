def simulate_hits(rotations):
    position = 50
    count_zero = 0
    for rot in rotations:
        direction = rot[0]
        distance = int(rot[1:])
        step = 1 if direction == "R" else -1
        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                count_zero += 1
    return count_zero

def count_password_hits(filepath: str) -> int:
    with open(filepath, "r") as f:
        rotations = [line.strip() for line in f if line.strip()]
    return simulate_hits(rotations)


# Example usage
example_input = [
    "L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"
]

print(simulate_hits(example_input))
print(count_password_hits("data/day01.txt"))
