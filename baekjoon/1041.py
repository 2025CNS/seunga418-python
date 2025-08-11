N = int(input())
dice = list(map(int, input().split()))
opposite = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
min1 = min(dice)
min2 = float('inf')
for i in range(6):
    for j in range(i + 1, 6):
        if j != opposite[i]:
            min2 = min(min2, dice[i] + dice[j])
min3 = float('inf')
triplets = [
    (0, 1, 2), (0, 1, 3), (0, 4, 2), (0, 4, 3),
    (5, 1, 2), (5, 1, 3), (5, 4, 2), (5, 4, 3)
]
for a, b, c in triplets:
    min3 = min(min3, dice[a] + dice[b] + dice[c])
if N == 1:
    print(sum(dice) - max(dice))
else:
    count3 = 4
    count2 = 8 * N - 12
    count1 = (5 * N - 6) * (N - 2)
    result = count3 * min3 + count2 * min2 + count1 * min1
    print(result)