from typing import List, Tuple
import pulp

def parse_machine(line: str) -> Tuple[List[List[int]], List[int]]:
    buttons = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == '(':
            j = i + 1
            while j < n and line[j] != ')':
                j += 1
            inside = line[i+1:j].strip()
            if inside:
                buttons.append(list(map(int, inside.split(','))))
            i = j + 1
        else:
            i += 1
    l = line.find('{')
    r = line.find('}', l + 1)
    target = list(map(int, line[l+1:r].split(',')))
    return buttons, target

def ilp_min_presses(buttons: List[List[int]], target: List[int]) -> int:
    m = len(target)
    k = len(buttons)
    A = [[0]*k for _ in range(m)]
    for j, btn in enumerate(buttons):
        for idx in btn:
            if 0 <= idx < m:
                A[idx][j] = 1
    for i in range(m):
        if target[i] > 0 and all(A[i][j] == 0 for j in range(k)):
            return -1
    if all(v == 0 for v in target):
        return 0
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(k)]
    prob = pulp.LpProblem("min_presses", pulp.LpMinimize)
    prob += pulp.lpSum(x)
    for i in range(m):
        prob += pulp.lpSum(A[i][j] * x[j] for j in range(k)) == target[i]
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != "Optimal":
        return -1
    return int(round(sum(var.value() for var in x)))

def total_min_presses_improved(lines: List[str]) -> int:
    total = 0
    for line in lines:
        buttons, target = parse_machine(line)
        presses = ilp_min_presses(buttons, target)
        if presses == -1:
            raise ValueError("Unsolvable machine: " + line)
        total += presses
    return total

def count_factory_improved(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    return total_min_presses_improved(lines)

example_input = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
]

print(total_min_presses_improved(example_input))
print(count_factory_improved("data/day10.txt"))
