r, g, b = map(int, input().split())
count = 0
for red in range(r):
    for green in range(g):
        for blue in range(b):
            print(red, green, blue)
            count += 1
print(count)