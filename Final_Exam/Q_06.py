def HashGet(table: list[list[tuple]], key):
    index = hash(key) % len(table)
    bucket = table[index]

    for k, v in bucket:
        if k == key:
            return v

    return None
