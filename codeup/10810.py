N_M_str = input().split()
N = int(N_M_str[0])
M = int(N_M_str[1])
baskets = [0] * N
for _ in range(M):
    i_j_k_str = input().split()
    i = int(i_j_k_str[0])
    j = int(i_j_k_str[1])
    k = int(i_j_k_str[2])
    for idx in range(i - 1, j):
        baskets[idx] = k
print(' '.join(map(str, baskets)))