A, B = map(int, input().split())
C = int(input())
min = A * 60 + B + C
hour = (min // 60) % 24
m = min % 60
print(hour, m)