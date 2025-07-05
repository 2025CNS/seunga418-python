import sys
input = sys.stdin.read
def main():
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    prefix = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = int(data[idx]) + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
            idx += 1
    result = []
    for _ in range(M):
        x1 = int(data[idx])
        idx += 1
        y1 = int(data[idx])
        idx += 1
        x2 = int(data[idx])
        idx += 1
        y2 = int(data[idx])
        idx += 1
        total = (prefix[x2][y2]
                - prefix[x1 - 1][y2]
                - prefix[x2][y1 - 1]
                + prefix[x1 - 1][y1 - 1])
        result.append(str(total))
    print("\n".join(result))
main()