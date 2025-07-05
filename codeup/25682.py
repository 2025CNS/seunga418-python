import sys
input = sys.stdin.readline
def make_chess_pattern(n, m, start_color):
    pattern = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                pattern[i][j] = start_color  # 시작 색
            else:
                pattern[i][j] = 'B' if start_color == 'W' else 'W'
    return pattern
def make_diff(board, pattern):
    n, m = len(board), len(board[0])
    diff = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != pattern[i][j]:
                diff[i][j] = 1
    return diff
def prefix_sum_2d(diff):
    n, m = len(diff), len(diff[0])
    psum = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            psum[i][j] = (
                diff[i-1][j-1]
                + psum[i-1][j]
                + psum[i][j-1]
                - psum[i-1][j-1]
            )
    return psum
def get_kxk_sum(psum, x1, y1, x2, y2):
    return (
        psum[x2][y2]
        - psum[x1][y2]
        - psum[x2][y1]
        + psum[x1][y1]
    )
N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
patternW = make_chess_pattern(N, M, 'W')
patternB = make_chess_pattern(N, M, 'B')
diffW = make_diff(board, patternW)
diffB = make_diff(board, patternB)
psumW = prefix_sum_2d(diffW)
psumB = prefix_sum_2d(diffB)
min_paint = float('inf')
for i in range(N - K + 1):
    for j in range(M - K + 1):
        x1, y1 = i, j
        x2, y2 = i + K, j + K
        paintW = get_kxk_sum(psumW, x1, y1, x2, y2)
        paintB = get_kxk_sum(psumB, x1, y1, x2, y2)
        min_paint = min(min_paint, paintW, paintB)
print(min_paint)