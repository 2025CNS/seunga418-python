import sys

A, B, C, D = map(int, sys.stdin.read().split())

total = A*3600 + B*60 + C
total = (total + D) % (24*3600)

h = total // 3600
m = (total % 3600) // 60
s = total % 60

print(h, m, s)