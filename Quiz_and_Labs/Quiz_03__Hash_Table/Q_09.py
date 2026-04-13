"""
Using the below code, identify the elements stored at each index of the hash table after the following operations are executed:


table = [[], [],[]]
HashInsert(table, 4, "A")
HashInsert(table, 1, "B")

table[1][0]
(4, 'A')

table[1][1]
(1, 'B')


"""


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
