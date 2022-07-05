from typing import List

N: int = int(input())
X: List[int] = []
Y: List[int] = []

for _ in range(N):
    x: int
    y: int
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

median_x: int = X[N // 2]
median_y: int = Y[N // 2]
ans: int = 0

for i in range(N):
    ans += abs(X[i] - median_x)
    ans += abs(Y[i] - median_y)
print(ans)
