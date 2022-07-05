from collections import deque

H, W = map(int, input().split())
start = [int(i) - 1 for i in input().split()]
goal = [int(i) - 1 for i in input().split()]
matrix = [input() for _ in range(H)]
INF = 10**9


def trans(h, w):
    return h * W + w


M = [False] * (trans(H, W))

for h in range(H):
    for w in range(W):
        M[trans(h, w)] = matrix[h][w] == "."


def is_ok(h, w):
    return 0 <= h < H and 0 <= w < W and M[trans(h, w)]


def bfs_01(start, goal):
    C = [INF] * (trans(H, W))
    sx, sy = start
    gx, gy = goal
    q = deque()
    q.append((sx, sy, -1, -1))
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]
    while q:
        x, y, c, d = q.popleft()
        now = trans(x, y)
        if c > C[now]:
            continue
        C[now] = c
        if x == gx and y == gy:
            break
        for i, (dx, dy) in enumerate(zip(DX, DY)):
            nx = x + dx
            ny = y + dy
            if is_ok(nx, ny):
                if d == (i + 2) % 4:
                    continue
                if d == i and c <= C[trans(nx, ny)]:
                    q.appendleft((nx, ny, c, i))
                elif c + 1 <= C[trans(nx, ny)]:
                    q.append((nx, ny, c + 1, i))
    return C[trans(gx, gy)]


print(bfs_01(start, goal))
