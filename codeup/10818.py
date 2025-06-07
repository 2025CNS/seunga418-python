N = int(input())
numbers = list(map(int, input().split()))
min = numbers[0]
max = numbers[0]
for num in numbers[1:]:
    if num < min:
        min = num
    if num > max:
        max = num
print(min, max)