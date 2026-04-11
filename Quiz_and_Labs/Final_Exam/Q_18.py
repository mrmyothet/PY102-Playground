from collections import deque


def first_non_repeating(stream: str) -> str:
    q = deque()
    count = {}
    result = []

    for ch in stream:
        count[ch] = count.get(ch, 0) + 1
        q.append(ch)

        while q and count[q[0]] > 1:
            q.popleft()

        if q:
            result.append(q[0])
        else:
            result.append("#")

    return "".join(result)
