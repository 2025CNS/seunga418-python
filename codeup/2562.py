max = 0
max_i = 0
for i in range(9):
    num = int(input())
    if num > max:
        max = num
        max_i = i + 1
print(max)
print(max_i)