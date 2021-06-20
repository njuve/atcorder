convert = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

S = list(map(int, input()))
print("".join([str(convert[_]) for _ in S][::-1]))
