import sys
it = list(map(int, sys.stdin.read().split()))
N = it[0]
idx = 1
best = 0
for _ in range(N):
    a, b, c = sorted(it[idx:idx+3])
    idx += 3
    if a == c:
        prize = 10000 + a * 1000
    elif a == b or b == c:
        same = a if a == b else c
        prize = 1000 + same * 100
    else:
        prize = c * 100
    best = max(best, prize)
print(best)