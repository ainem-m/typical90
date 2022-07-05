from typing import List

H: int
W: int
H, W = map(int, input().split())
matrix: List[List[int]] = [[int(i) for i in input().split()] for _ in range(H)]

sums_row: List[int] = [sum(r) for r in matrix]
sums_col: List[int] = [sum(c) for c in zip(*matrix)]

ans: List[List[int]] = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = sums_row[i] + sums_col[j] - matrix[i][j]
for i in range(H):
    print(" ".join((str(a) for a in ans[i])))
