import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
def divide_and_count(x, y, size):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half = size // 2
                divide_and_count(x, y, half)
                divide_and_count(x, y + half, half)
                divide_and_count(x + half, y, half)
                divide_and_count(x + half, y + half, half)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
divide_and_count(0, 0, n)
print(white)
print(blue)