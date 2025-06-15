a, b = input().split()
a_reversed = int(a[::-1])
b_reversed = int(b[::-1])
print(max(a_reversed, b_reversed))