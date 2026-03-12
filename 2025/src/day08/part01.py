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
    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

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

def largest_three_product(lines: List[str], k: int=1000) -> int:
    coords = parse_input(lines)
    pairs = compute_pairs(coords)
    pairs.sort(key=lambda x: x[0])
    dsu = DSU(len(coords))
    for _, i, j in pairs[:k]:
        dsu.union(i, j)
    sizes = []
    seen = set()
    for i in range(len(coords)):
        root = dsu.find(i)
        if root not in seen:
            seen.add(root)
            sizes.append(dsu.size[root])
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def run_day8(filepath: str) -> int:
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return largest_three_product(lines, k=1000)

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

print(largest_three_product(example_input, k=10))
print(run_day8("data/day08.txt"))
