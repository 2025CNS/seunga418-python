from collections import deque
def min_operations(N):
    if N == 1:
        return 0
    visited = set()
    queue = deque()
    queue.append((1, 0))
    while queue:
        current, steps = queue.popleft()
        if current == N:
            return steps
        if current + 1 not in visited and current + 1 <= N:
            visited.add(current + 1)
            queue.append((current + 1, steps + 1))
        if current > 1 and current - 1 not in visited:
            visited.add(current - 1)
            queue.append((current - 1, steps + 1))
        power = current * current
        while power <= N:
            if power not in visited:
                visited.add(power)
                queue.append((power, steps + 1))
            power *= current
    return -1
N = int(input())
print(min_operations(N))