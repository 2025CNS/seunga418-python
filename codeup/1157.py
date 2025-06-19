word = input().upper()
alphabet_c = {}
for ch in word:
    if ch in alphabet_c:
        alphabet_c[ch] += 1
    else:
        alphabet_c[ch] = 1
max_c = max(alphabet_c.values())
most_a = [k for k, v in alphabet_c.items() if v == max_c]
if len(most_a) > 1:
    print("?")
else:
    print(most_a[0])