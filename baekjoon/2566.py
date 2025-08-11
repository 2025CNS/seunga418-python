value = -1
row1 = 0
col = 0
for i in range(9):
    row2 = list(map(int, input().split()))
    for j in range(9):
        if row2[j] > value:
            value = row2[j]
            row1 = i + 1
            col = j + 1
print(value)
print(row1, col)