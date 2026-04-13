"""
The above hash function will work well for hashing 6-digit employee IDs into a hash table of size 20,000.

- True
- False

"""


def hashFunction1(key):
    return key % 1000
