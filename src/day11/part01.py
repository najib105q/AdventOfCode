from typing import List, Dict

def count_paths(graph: Dict[str, List[str]], start: str, end: str) -> int:
    memo = {}

    def dfs(node: str) -> int:
        if node == end:
            return 1
        if node in memo:
            return memo[node]
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt)
        memo[node] = total
        return total

    return dfs(start)


def parse_graph(lines: List[str]) -> Dict[str, List[str]]:
    graph = {}
    for line in lines:
        if not line.strip():
            continue
        name, rest = line.split(":")
        outputs = rest.strip().split()
        graph[name.strip()] = outputs
    return graph


def solve(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    graph = parse_graph(lines)
    return count_paths(graph, "you", "out")


example_input = [
    "aaa: you hhh",
    "you: bbb ccc",
    "bbb: ddd eee",
    "ccc: ddd eee fff",
    "ddd: ggg",
    "eee: out",
    "fff: out",
    "ggg: out",
    "hhh: ccc fff iii",
    "iii: out",
]

print(count_paths(parse_graph(example_input), "you", "out"))
print(solve("data/day11.txt"))
