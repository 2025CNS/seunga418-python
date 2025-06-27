def a(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
M = int(input())
N = int(input())
p = []
for num in range(M, N + 1):
    if a(num):
        p.append(num)
if p:
    print(sum(p))
    print(min(p))
else:
    print(-1)