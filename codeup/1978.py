def a(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
N = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if a(num):
        count += 1
print(count)