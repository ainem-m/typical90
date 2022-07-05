from itertools import accumulate as acc
n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

B = [0] +  list(acc(A))
ans = 0
for i in range(k, n):
  ans = max(ans, B[i]-B[i-k])
print(ans)