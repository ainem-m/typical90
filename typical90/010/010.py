from math import gcd
from operator import add, mul, xor, or_, and_
import sys
from typing import Union, List, Dict

input = sys.stdin.readline


class monoid:
    """
    結合律 ope(ope(a, b), c) == ope(a, ope(b+c))を満たし
    単位元 ope(a, identity) == aが存在するもの

    ope: function(a, b)
    identity: int

    ex) 和 (A+B)+C = A+(B+C), A+0 = A
        積 (A*B)*C = A*(B*C), A*1 = A
    """

    def __init__(self, ope, identity: Union[int, float]) -> None:
        self.ope = ope
        self.identity = identity


monoid_list: Dict[str, monoid] = {
    "min": monoid(min, float("inf")),
    "max": monoid(max, -float("inf")),
    "sum": monoid(add, 0),
    "mul": monoid(mul, 1),
    "xor": monoid(xor, 0),
    "or": monoid(or_, 0),
    "and": monoid(and_, (1 << 60) - 1),
    "gcd": monoid(gcd, 0),
}


class SegmentTree:
    """monoid:monoid, n:int

    クエリの添字は0-indexedで受け取る
    Args:
      monoid(monoid): monoid(行う計算, 単位元) monoid_listを参照
      n(int): 配列のサイズ、セグ木のサイズはこの２倍になる
    """

    def __init__(self, monoid: monoid, n:int):
        self.n = n
        self.ope = monoid.ope
        self.identity = monoid.identity
        self.seg = [self.identity] * (2 * self.n)

    def build(self, array:List):
        assert len(array) == self.n
        self.seg[self.n : 2 * self.n] = array
        for i in range(1, self.n)[::-1]:
            self.seg[i] = self.ope(self.seg[i << 1 | 0], self.seg[i << 1 | 1])

    def set(self, i: int, x: int):
        """i番目(0-indexed)に値をセットする

        Args:
            i (int): 0-indexed
            x (int)
        """
        i += self.n
        self.seg[i] = x
        while i > 1:
            i >>= 1
            self.seg[i] = self.ope(self.seg[i << 1 | 0], self.seg[i << 1 | 1])

    def get(self, l: int, r: int) -> Union[int, float]:
        """区間での処理を行った値を返す
        [l,r)の半開区間であることに注意

        Args:
            l (int): 0-indexed
            r (int): 0-indexed

        Returns:
            int: 処理結果

            ex) "sum"：区間和 "min":区間内の最小値
        """
        l += self.n
        r += self.n
        tmp = self.identity
        while l < r:
            if l & 1:
                tmp = self.ope(tmp, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                tmp = self.ope(self.seg[r], tmp)
            l >>= 1
            r >>= 1
        return tmp


if __name__ == "__main__":
    n = int(input())
    seg1: SegmentTree = SegmentTree(monoid_list["sum"], n=n + 1)
    seg2: SegmentTree = SegmentTree(monoid_list["sum"], n=n + 1)
    S: List[SegmentTree] = [seg1, seg2]
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        S[a - 1].set(i, b)
    q = int(input())
    for qi in range(q):
        l, r = map(int, input().split())
        print(S[0].get(l, r + 1), S[1].get(l, r + 1))
