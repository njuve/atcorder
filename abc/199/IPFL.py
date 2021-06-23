N = int(input())
S = list(input())
Q = int(input())
qs = [list(map(int, input().split())) for _ in range(Q)]
is_reverse = False
for q in qs:
    a = q[1] - 1
    b = q[2] - 1
    if q[0] == 1:
        if is_reverse:
            a = a + N if a <= N else a - N
            b = b + N if b <= N else b - N
            S[a], S[b] = S[b], S[a]
        else:
            S[a], S[b] = S[b], S[a]
    elif q[0] == 2:
        is_reverse = not bool(is_reverse)
if is_reverse:
    S[N:], S[:N] = S[:N], S[N:]
print("".join(S))
