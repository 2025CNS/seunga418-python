a, b, c = map(int, input())
d, e, f = map(int, input())
num1 = a * 100 + b * 10 + c
print(num1 * f)
print(num1 * e)
print(num1 * d)
print(num1 * (d * 100 + e * 10 + f))