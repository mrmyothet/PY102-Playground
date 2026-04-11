def insert_linear_probing(table: list[int | None], key: int) -> list[int | None]:
    n = len(table)
    idx = key % n

    for _ in range(n):
        if table[idx] is None:
            table[idx] = key
            return table
        idx = (idx + 1) % n

    return table
