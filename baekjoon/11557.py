import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    best_name, best_val = "", -1
    for _ in range(n):
        s, l = input().split()
        l = int(l)
        if l > best_val:
            best_val = l
            best_name = s
    print(best_name)