import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
prefix_sum = 0
count = [0] * m
count[0] = 1
answer = 0
for num in a:
    prefix_sum = (prefix_sum + num) % m
    answer += count[prefix_sum]
    count[prefix_sum] += 1
print(answer)