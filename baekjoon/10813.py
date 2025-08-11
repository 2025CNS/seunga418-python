N_M_str = input().split()
N = int(N_M_str[0])
M = int(N_M_str[1])
baskets = []
for i in range(1, N + 1):
    baskets.append(i)
for _ in range(M):
    i_j_str = input().split()
    i = int(i_j_str[0])
    j = int(i_j_str[1])
    temp = baskets[i - 1] 
    baskets[i - 1] = baskets[j - 1] 
    baskets[j - 1] = temp 
print(' '.join(map(str, baskets)))