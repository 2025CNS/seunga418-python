import sys

it = iter(sys.stdin.read().strip().splitlines())
T = int(next(it))
ops = {'@': lambda x: x * 3, '%': lambda x: x + 5, '#': lambda x: x - 7}

out = []
for _ in range(T):
    tokens = next(it).split()
    val = float(tokens[0])
    for t in tokens[1:]:
        val = ops[t](val)
    out.append(f"{val:.2f}")

print("\n".join(out))