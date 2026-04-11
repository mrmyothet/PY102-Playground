from collections import deque


def hot_potato(names: list[str], k: int) -> str:
    q = deque(names)

    while len(q) > 1:
        for _ in range(k):
            q.append(q.popleft())
        q.popleft()
    return q[0]
