import sys
def solve():
    N = int(sys.stdin.readline())
    F = int(sys.stdin.readline())
    base_N = (N // 100) * 100
    for i in range(100):
        current_N = base_N + i
        if current_N % F == 0:
            print(f"{i:02d}")
            return
solve()