n = int(input())
video = [input().strip() for _ in range(n)]
def compress(x, y, size):
    first = video[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != first:
                same = False
                break
        if not same:
            break
    if same:
        return first
    else:
        half = size // 2
        return "(" + \
               compress(x, y, half) + \
               compress(x, y + half, half) + \
               compress(x + half, y, half) + \
               compress(x + half, y + half, half) + ")"
print(compress(0, 0, n))