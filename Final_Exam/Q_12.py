def HashInsert(table: list[list[tuple]], key, value) -> None:
    index = hash(key) % len(table)
    bucket = table[index]

    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return

    bucket.append((key, value))


def h(key):
    return key % 3


def HashGet(table: list[list[tuple]], key):
    index = hash(key) % len(table)
    bucket = table[index]

    for k, v in bucket:
        if k == key:
            return v

    return None
