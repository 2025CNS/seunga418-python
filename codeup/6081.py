n = input().strip()
n_decimal = int(n, 16)
for i in range(1, 16):
    print(f'{n}*{format(i, "X")}={format(n_decimal * i, "X")}')