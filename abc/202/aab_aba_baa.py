# all xxxx is axxx or bxxx
# Set A = #a, B = #b
# Set c = C(A-1+B, B) = #xxxx s.t. axxx
# if c >= k, xxxx = axxx
# if c < k, xxxx = bxxx

A, B, K = map(int, input().split())
DP = [[0] * (B + 2) for _ in range(A + 2)]
DP[0][0] = 1
for i in range(A + 1):
    for j in range(B + 1):
        DP[i + 1][j] += DP[i][j]
        DP[i][j + 1] += DP[i][j]

result = ""
print(DP)
for _ in range(A + B):
    if (A == 0) or (B == 0):
        break
    elif DP[A - 1][B] >= K:
        result = result + "a"
        A = A - 1
    elif DP[A - 1][B] < K:
        result = result + "b"
        K = K - DP[A - 1][B]
        B = B - 1
    print(f"result = {result}")

result = result + A * "a"
result = result + B * "b"
print(result)