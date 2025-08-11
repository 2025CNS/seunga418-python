import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
sorted_unique = sorted(set(arr))
def binary_search(x):
    left, right = 0, len(sorted_unique) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_unique[mid] == x:
            return mid
        elif sorted_unique[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
result = []
for x in arr:
    result.append(str(binary_search(x)))
print(' '.join(result))