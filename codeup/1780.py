import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count = {-1: 0, 0: 0, 1: 0}
def check(x, y, size):
    current = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != current:
                new_size = size // 3
                for dx in range(3):
                    for dy in range(3):
                        check(x + dx * new_size, y + dy * new_size, new_size)
                return
    count[current] += 1
check(0, 0, n)
print(count[-1])
print(count[0])
print(count[1])