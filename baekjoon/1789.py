S = int(input().strip())
total = 0
n = 0
while total <= S:
    n += 1
    total += n
print(n - 1)