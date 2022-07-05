from itertools import accumulate as acc

n, k = map(int, input().split())
C = [0]
for _ in range(n-1):
  C.append(int(input()))
C = list(acc(C))

ans = 0
cur = 0

for _ in range(k):
  move = int(input())
  ans += abs(C[cur]-C[cur+move])
  cur += move
  # print(cur, ans)
print(ans%100000)