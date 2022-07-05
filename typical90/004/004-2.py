from collections import Counter
from typing import List, Final

n: int = int(input())
MOD: Final[int] = 10**9+7

fact:List[int] = [1, 1]
fact_inv:List[int] = [1, 1]
for i in range(2, 10**5+1):
    fact.append(fact[-1]*i%MOD)
    fact_inv.append(pow(fact[-1], MOD-2, MOD))

def comb(a:int, b:int) -> int:
    """returns num of combinations(a, b):aCb
    a!/b!(a-b)!
    Args:
        a (int)
        b (int)

    Returns:
        int: 
    """
    if a<b: a, b = b, a
    return (fact[a]*fact_inv[b]*fact_inv[a-b])%MOD

A: List[int] = [int(i) for i in input().split()]
key: int = Counter(A).most_common()[0][0]
ante: int = A.index(key)
post: int = n - A.index(key, ante+1)

first: int = max(ante, post)
second: int = min(ante, post)
#print(first, second)
for i in range(1, n+2):
    ans:int = comb(len(A), i)
    if i-1<=first+second:
        ans -= comb(first+second, i-1)
    print(ans)