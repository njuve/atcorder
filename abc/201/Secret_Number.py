import itertools

S = input()
iin = set(i for i in range(10) if S[i] == "o")
inotin = set(i for i in range(10) if S[i] == "x")

ans = 0
for p in itertools.product(*[range(10) for _ in range(4)]):
    seq = set(p)
    if len(inotin & seq) > 0 or len(iin & seq) < len(iin):
        continue
    ans += 1
print(ans)