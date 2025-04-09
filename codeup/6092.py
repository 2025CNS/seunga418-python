n = int(input())
a = list(map(int, input().split()))
d = [0] * 24
for i in range(n):
    d[a[i]] += 1
print(*d[1:24])