N = int(input())
count = 0

for _ in range(N):
    word = input()
    seen = set()
    prev_char = ''
    is_group = True

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group = False
                break
            seen.add(char)
        prev_char = char

    if is_group:
        count += 1

print(count)