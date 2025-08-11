import sys
import math
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
max_square = -1
for r in range(N):
    for c in range(M):
        for dr in range(-N, N):
            for dc in range(-M, M):
                if dr == 0 and dc == 0:
                    continue
                num_str = ''
                rr, cc = r, c
                while 0 <= rr < N and 0 <= cc < M:
                    num_str += board[rr][cc]
                    num = int(num_str)
                    root = int(math.isqrt(num))
                    if root * root == num:
                        max_square = max(max_square, num)
                    rr += dr
                    cc += dc
print(max_square)