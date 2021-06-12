# pypy3

# Set S = T_1 + \cdots + T_N
# Set I \subset {1, \dots, N}
# Then (time1, time2) = (\sum_{i \in I}T_i, S - \sum_{i \in I}T_i)
# Suppose that \sum_{i \in I}T_i < S - \sum_{i \in I}T_i
# We will find I such that S - \sum_{i \in I}T_i is min (i.e., \sum_{i \in I}T_i is max)
# Since \sum_{i \in I}T_i < S/2,
# it is suffice to find I such that \sum_{i \in I}T_i is max
# and \sum_{i \in I}T_i < S/2

N = int(input())
T = list(map(int, input().split()))
S = sum(T)
dp = [[0] * (S // 2 + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    dp[i][0] = 1
    for t in range(S // 2 + 1):
        if t - T[i] >= 0:
            dp[i + 1][t] = max(dp[i][t - T[i]], dp[i][t])
        else:
            dp[i + 1][t] = dp[i][t]

maxtime = 0
for t in range(S // 2 + 1):
    if dp[N][t] == 1:
        maxtime = t

print(S - maxtime)