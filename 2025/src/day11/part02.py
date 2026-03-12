from typing import Dict, List, Tuple

def count_required_paths(graph: Dict[str, List[str]], start: str, end: str,
                         required: List[str]) -> int:
    memo = {}

    def dfs(node: str, seen_dac: bool, seen_fft: bool) -> int:
        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]

        if node == end:
            memo[key] = 1 if (seen_dac and seen_fft) else 0
            return memo[key]

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(
                nxt,
                seen_dac or (node == required[0]),
                seen_fft or (node == required[1])
            )

        memo[key] = total
        return total

    return dfs(start, False, False)


def parse_graph(lines: List[str]) -> Dict[str, List[str]]:
    graph = {}
    for line in lines:
        if not line.strip():
            continue
        name, rest = line.split(":")
        graph[name.strip()] = rest.strip().split()
    return graph


def solve(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    graph = parse_graph(lines)
    return count_required_paths(graph, "svr", "out", ["dac", "fft"])


example_input = [
    "svr: aaa bbb",
    "aaa: fft",
    "fft: ccc",
    "bbb: tty",
    "tty: ccc",
    "ccc: ddd eee",
    "ddd: hub",
    "hub: fff",
    "eee: dac",
    "dac: fff",
    "fff: ggg hhh",
    "ggg: out",
    "hhh: out",
]

print(count_required_paths(parse_graph(example_input), "svr", "out", ["dac", "fft"]))
print(solve("data/day11.txt"))
