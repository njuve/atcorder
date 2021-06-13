N, K = map(int, input().split())
print(sum([100 * i + j for i in range(N) for j in range(M)]))