N, B = map(int, input().split())
r = ''
while N > 0:
    re = N % B
    if re < 10:
        r = str(re) + r
    else:
        r = chr(re - 10 + ord('A')) + r
    N //= B
print(r)