import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
data = list(map(int, sys.stdin.read().split()))
T = data[0]
ans = []
i = 1
for _ in range(T):
    A, B = data[i], data[i+1]
    i += 2
    g = gcd(A, B)
    ans.append(str(A // g * B))
print('\n'.join(ans))