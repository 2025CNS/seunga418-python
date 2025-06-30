while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    s = sorted([a, b, c])
    if s[2] >= s[0] + s[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")