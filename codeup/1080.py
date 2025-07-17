import sys
def solve():
    N, M = map(int, sys.stdin.readline().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, list(sys.stdin.readline().strip()))))
    B = []
    for _ in range(N):
        B.append(list(map(int, list(sys.stdin.readline().strip()))))
    count = 0
    def flip_submatrix(r, c):
        for x in range(r, r + 3):
            for y in range(c, c + 3):
                A[x][y] = 1 - A[x][y]
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip_submatrix(i, j)
                count += 1
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                print(-1)
                return
    print(count)
solve()