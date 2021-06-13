N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[0])
for ab in AB:
    if K < ab[0]:
        break
    else:
        K = K + ab[1]

print(K)