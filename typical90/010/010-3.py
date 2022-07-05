from itertools import accumulate as acc
n = int(input())
A = [int(i) for i in input().split()]
B = list(acc(A))
ans = 0
MOD = 10**9+7
for i, a in enumerate(A[:0:-1],1):
  ans += a*B[~i]
  ans %= MOD
print(ans)