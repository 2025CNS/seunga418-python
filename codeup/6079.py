n = int(input())
sum_1 = 0
cnt = 0

for i in range(1,n+1):
    cnt += 1
    sum_1 += i
    if sum_1>=n:
        print(cnt)
        break