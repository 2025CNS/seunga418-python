word = input()
croatian = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
for c in croatian:
    word = word.replace(c, "X")
print(len(word))