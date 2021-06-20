from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
Ad = defaultdict(lambda: 0)
for a in A:
    Ad[a] = Ad[a] + 1
BC = [B[c - 1] for c in C]
result = 0
for b in BC:
    result = result + Ad[b]

print(result)
