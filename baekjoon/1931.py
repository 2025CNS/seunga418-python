import sys
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
meetings = [tuple(map(int, line.split())) for line in data[1:]]
meetings.sort(key=lambda x: (x[1], x[0]))
count = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end
print(count)