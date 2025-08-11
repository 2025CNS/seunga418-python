p = [tuple(map(int, input().split())) for _ in range(3)]
x = [i[0] for i in p]
y = [i[1] for i in p]
for j in x:
    if x.count(j) == 1:
        x1 = j
        break
for k in y:
    if y.count(k) == 1:
        y1 = k
        break
print(x1, y1)