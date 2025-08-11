import sys
input = sys.stdin.read

data = input().split()
N, M = int(data[0]), int(data[1])
A = list(map(int, data[2:N+2]))

# 누적합 배열 생성
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i-1] + A[i-1]

# 질의 처리
result = []
idx = N + 2
for _ in range(M):
    i, j = int(data[idx]), int(data[idx + 1])
    result.append(str(S[j] - S[i-1]))
    idx += 2

print('\n'.join(result))
