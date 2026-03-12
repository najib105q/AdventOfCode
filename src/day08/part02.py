from typing import List, Tuple
import math

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def parse_input(lines: List[str]) -> List[Tuple[int,int,int]]:
    return [tuple(map(int, line.split(","))) for line in lines]

def compute_pairs(coords: List[Tuple[int,int,int]]) -> List[Tuple[float,int,int]]:
    pairs = []
    n = len(coords)
    for i in range(n):
        for j in range(i+1, n):
            x1,y1,z1 = coords[i]
            x2,y2,z2 = coords[j]
            d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            pairs.append((d,i,j))
    return pairs

def last_connection_product(lines: List[str]) -> int:
    coords = parse_input(lines)
    pairs = compute_pairs(coords)
    pairs.sort(key=lambda x: x[0])
    dsu = DSU(len(coords))
    connected = 1
    last_pair = None
    for _, i, j in pairs:
        if dsu.union(i, j):
            connected += 1
            last_pair = (i, j)
            if connected == len(coords):
                break
    x1 = coords[last_pair[0]][0]
    x2 = coords[last_pair[1]][0]
    return x1 * x2

def run_day8_compact(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return last_connection_product(lines)

example_input = [
"162,817,812",
"57,618,57",
"906,360,560",
"592,479,940",
"352,342,300",
"466,668,158",
"542,29,236",
"431,825,988",
"739,650,466",
"52,470,668",
"216,146,977",
"819,987,18",
"117,168,530",
"805,96,715",
"346,949,466",
"970,615,88",
"941,993,340",
"862,61,35",
"984,92,344",
"425,690,689"
]

print(last_connection_product(example_input))
print(run_day8_compact("data/day08.txt"))
