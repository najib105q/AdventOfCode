from typing import List, Tuple
from collections import deque

def parse_machine(line: str) -> Tuple[List[int], List[List[int]]]:
    diagram = line.split(']')[0].strip('[')
    target = [1 if ch == '#' else 0 for ch in diagram]
    parts = line.split(')')
    buttons = []
    for part in parts:
        if '(' in part:
            inside = part.split('(')[1]
            if inside.strip():
                buttons.append(list(map(int, inside.split(','))))
    return target, buttons

def min_button_presses(target: List[int], buttons: List[List[int]]) -> int:
    n = len(target)
    start = tuple([0]*n)
    target = tuple(target)
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        state, presses = queue.popleft()
        if state == target:
            return presses
        for btn in buttons:
            new_state = list(state)
            for idx in btn:
                new_state[idx] ^= 1
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses+1))
    return -1

def total_min_presses(lines: List[str]) -> int:
    total = 0
    for line in lines:
        target, buttons = parse_machine(line)
        total += min_button_presses(target, buttons)
    return total

def count_factory(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    return total_min_presses(lines)

example_input = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
]

print(total_min_presses(example_input))
print(count_factory("data/day10.txt"))
