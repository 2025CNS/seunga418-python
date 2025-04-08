import math
def lcm(a, b):
    return (a * b) // math.gcd(a, b)
a, b, c = map(int, input().split())
result = lcm(lcm(a, b), c)

print(result)