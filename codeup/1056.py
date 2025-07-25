import heapq
import math
def solve(N):
    if N == 1:
        return 0
    visited = {}
    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        ops, current = heapq.heappop(heap)
        if current == N:
            return ops
        if current in visited and visited[current] <= ops:
            continue
        visited[current] = ops
        if current + 1 <= N:
            heapq.heappush(heap, (ops + 1, current + 1))
        if current > 1:
            heapq.heappush(heap, (ops + 1, current - 1))
        max_k = 64
        power = current * current
        while power <= N:
            heapq.heappush(heap, (ops + 1, power))
            if current == 1:
                break
            power *= current
    return -1