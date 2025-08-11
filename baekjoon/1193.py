X = int(input())
line = 1
total = 0
while total + line < X:
    total += line
    line += 1
position = X - total
if line % 2 == 0:
    nu = position
    de = line - position + 1
else:
    nu = line - position + 1
    de = position
print(f"{nu}/{de}")