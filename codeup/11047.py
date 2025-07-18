import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
count = 0
for coin in reversed(coins):
    if K == 0:
        break
    count += K // coin
    K %= coin
print(count)