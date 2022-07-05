from collections import defaultdict
from typing import List, Tuple

H:int; W:int
H, W = map(int, input().split())
matrix:List[List[int]] = [[int(i) for i in input().split()] for _ in range(H)]

C:defaultdict[int, defaultdict[int, int]] = defaultdict(lambda: defaultdict(int))

# 行の選び方をbit全探索(最大256通り)し、列ごとにすべて同じ数字であればカウント

def cnt_all_same(bit:int, w:int) -> Tuple[int, int]:
  cnt:int = 0
  tmp:int = -1
  for h in range(H):
    if (bit>>h) & 1:
      if tmp < 0: tmp = matrix[h][w]
      elif tmp != matrix[h][w]: return -1, 0
      cnt += 1
  return tmp, cnt

for bit in range(1<<H):
  for w in range(W):
    tmp, cnt = cnt_all_same(bit, w)
    C[bit][tmp] += cnt
ans:int = 0
for key in C.keys():
  if C[key]:
    ans = max(ans, max(C[key].values()))
print(ans)