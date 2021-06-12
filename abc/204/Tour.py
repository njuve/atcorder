import sys

sys.setrecursionlimit(10000)


def dfs(G, i, done):
    if done[i]:
        return
    done[i] = True
    for j in G[i]:
        dfs(G, j, done)


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)

result = 0
for i in range(N):
    done = [False] * N
    dfs(G, i, done)
    result = result + sum(done)

print(result)