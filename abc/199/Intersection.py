N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(len([_ for _ in range(max(A), min(B) + 1)]))
