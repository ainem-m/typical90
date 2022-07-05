from math import gcd
from functools import reduce


A = [int(i) for i in input().split()]
gcd_A = reduce(gcd, A)
ans = 0
for a in A:
    ans += a // gcd_A - 1
print(ans)
