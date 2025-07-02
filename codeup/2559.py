a, b = map(int, input().split())
t = list(map(int, input().split()))
window_sum = sum(t[:b])
max_sum = window_sum
for i in range(b, a):
    window_sum = window_sum - t[i - b] + t[i]
    max_sum = max(max_sum, window_sum)
print(max_sum)