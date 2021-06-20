N = int(input())
_ST = [input().split() for _ in range(N)]
ST = {kv[0]: int(kv[1]) for kv in _ST}

print(sorted(ST.items(), key=lambda x: x[1])[-2][0])
