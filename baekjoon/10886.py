import sys
data = list(map(int, sys.stdin.read().split()))
N, votes = data[0], data[1:]
cnt1 = sum(votes[:N])
print("Junhee is cute!" if cnt1 > N // 2 else "Junhee is not cute!")