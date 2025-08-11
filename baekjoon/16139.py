import sys
input = sys.stdin.read
data = input().split()
S = data[0]
q = int(data[1])
queries = data[2:]
n = len(S)
prefix = [[0] * 26 for _ in range(n + 1)]
for i in range(n):
    for j in range(26):
        prefix[i + 1][j] = prefix[i][j]
    prefix[i + 1][ord(S[i]) - ord('a')] += 1
output = []
for i in range(q):
    ch = queries[i * 3]
    l = int(queries[i * 3 + 1])
    r = int(queries[i * 3 + 2])
    idx = ord(ch) - ord('a')
    cnt = prefix[r + 1][idx] - prefix[l][idx]
    output.append(str(cnt))
print('\n'.join(output))