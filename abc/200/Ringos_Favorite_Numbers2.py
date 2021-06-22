# a - b = 200n
# 200q_a + r_a - 200q_b - r_b = 200n
# 200(q_a - q_b) + r_a - r_b = 200n
# Then we have r_a - r_b = 200m
# Since 0 <= r_a, r_b < 200, r_a - r_b = 0

N = int(input())
A = list(map(int, input().split()))
R = [a % 200 for a in A]
cnt = [0] * 200
ans = 0
for r in R:
    ans += cnt[r]
    cnt[r] += 1

print(ans)
