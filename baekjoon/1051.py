import sys
def solve():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(sys.stdin.readline().strip()))))
    max_area = 1
    for i in range(N):
        for j in range(M):
            max_k = min(N - 1 - i, M - 1 - j)
            for k in range(max_k + 1):
                if (board[i][j] == board[i][j+k] and
                    board[i][j] == board[i+k][j] and
                    board[i][j] == board[i+k][j+k]):
                    current_side_length = k + 1
                    current_area = current_side_length * current_side_length
                    max_area = max(max_area, current_area)
    print(max_area)
solve()