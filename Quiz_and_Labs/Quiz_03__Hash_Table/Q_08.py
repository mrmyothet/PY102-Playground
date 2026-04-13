"""
The above hash functionwill work well for hashing "house selling prices" into a hash table of size 1000.


- True
- False

"""


def hashFunction(key):
    return key % 1000
