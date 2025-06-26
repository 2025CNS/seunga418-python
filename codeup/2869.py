a, b, c = map(int, input().split())
d = (c - a) // (a - b)
if (c - a) % (a - b) != 0:
    d += 1
print(d + 1)