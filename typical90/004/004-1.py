# https://atcoder.jp/contests/abc129/tasks/abc129_d
from typing import List

H:int
W:int
H, W = map(int, input().split())
H += 1; W += 1
matrix: List[str] = [input()+"#" for _ in range(H-1)]
matrix.append("#"*W)
horizontal: List[List[int]] = [[0 for _ in range(W)] for _ in range(H)]
vertical: List[List[int]] = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    tmp: int = 0
    for j in range(W):
        if matrix[i][j] == ".":
            tmp += 1
            horizontal[i][j] = tmp
        else:
            w = j-1
            while w >= 0 and horizontal[i][w]>0:
                horizontal[i][w] = tmp
                w -= 1
            tmp = 0
                
for j in range(W):
    tmp = 0
    for i in range(H):
        if matrix[i][j] == ".":
            tmp += 1
            vertical[i][j] = tmp
        else:
            h = i-1
            while h >= 0 and vertical[h][j]>0:
                vertical[h][j] = tmp
                h -= 1
            tmp = 0

ans: int = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, horizontal[i][j] + vertical[i][j] - 1)
print(ans)