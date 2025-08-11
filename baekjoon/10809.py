S = input()
positions = [-1] * 26

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')
    if positions[idx] == -1:
        positions[idx] = i

print(*positions)