n = int(input())
p = list(map(int, input().split()))
p.sort()
total_time = 0
current_time = 0
for time in p:
    current_time += time
    total_time += current_time
print(total_time)