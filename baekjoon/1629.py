def power(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    half = power(a, b // 2, c)
    result = (half * half) % c
    if b % 2 == 1:
        result = (result * a) % c
    return result
A, B, C = map(int, input().split())
print(power(A, B, C))