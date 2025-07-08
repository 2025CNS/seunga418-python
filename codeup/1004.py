import math
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for __ in range(n):
        cx, cy, r = map(int, input().split())
        dist_start = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        dist_end = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
        if (dist_start < r) != (dist_end < r):
            count += 1
    print(count)