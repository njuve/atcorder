A = list(map(int, input().split()))
A = sorted(A)
ans = "No"
if (A[1] - A[0]) == (A[2] - A[1]):
    ans = "Yes"

print(ans)
