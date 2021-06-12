N = int(input())
trees = list(map(int, input().split()))
print(sum([tree - 10 for tree in trees if tree > 10]))
N = int(input())