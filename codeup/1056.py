import collections
import sys
def solve():
    N = int(sys.stdin.readline())
    if N == 1:
        print(0)
        return
    q = collections.deque([(1, 0)])
    dist = {1: 0}
    min_ops_to_N = abs(N - 1)
    MAX_OPS_ESTIMATE = 70
    while q:
        curr_num, curr_ops = q.popleft()
        if curr_ops >= min_ops_to_N:
            continue
        min_ops_to_N = min(min_ops_to_N, curr_ops + abs(N - curr_num))
        next_num_plus_1 = curr_num + 1
        if next_num_plus_1 <= N + min_ops_to_N + 5:
            if next_num_plus_1 not in dist or dist[next_num_plus_1] > curr_ops + 1:
                dist[next_num_plus_1] = curr_ops + 1
                q.append((next_num_plus_1, curr_ops + 1))
        next_num_minus_1 = curr_num - 1
        if next_num_minus_1 >= 1:
            if next_num_minus_1 not in dist or dist[next_num_minus_1] > curr_ops + 1:
                dist[next_num_minus_1] = curr_ops + 1
                q.append((next_num_minus_1, curr_ops + 1))
        for x in range(2, 61):
            if curr_num in [0, 1]:
                next_num_power = curr_num
            else:
                next_num_power = curr_num ** x
            if next_num_power == curr_num:
                continue
            if curr_ops + 1 + abs(next_num_power - N) >= min_ops_to_N:
                break 
            min_ops_to_N = min(min_ops_to_N, curr_ops + 1 + abs(next_num_power - N))
            if next_num_power <= N + min_ops_to_N + 5:
                if next_num_power not in dist or dist[next_num_power] > curr_ops + 1:
                    dist[next_num_power] = curr_ops + 1
                    q.append((next_num_power, curr_ops + 1))
            else:
                break 
    print(min_ops_to_N)
solve()