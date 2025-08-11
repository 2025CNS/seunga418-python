N, L = map(int, input().split())
found = False
for length in range(L, 101):
    temp = N - (length * (length - 1)) // 2
    if temp % length == 0:
        start = temp // length
        if start >= 0:
            sequence = [str(start + i) for i in range(length)]
            print(" ".join(sequence))
            found = True
            break
if not found:
    print(-1)