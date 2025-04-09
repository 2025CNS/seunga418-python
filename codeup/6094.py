board = [[0] * 19 for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1
for row in board:
    print(*row)