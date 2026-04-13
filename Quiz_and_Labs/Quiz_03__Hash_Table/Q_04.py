"""
The above hash function is used for hashing 5-digit customer ID into a hash table of size 250. Choose the best statement.

- It will perform well if the customer IDs are sequential or patterned IDs.
- It will perform well because the hash values range from 0 to 249, matching the table size.
- It will not perform well if the customer IDs are sequential or patterned IDs.

"""


def hashFunction(key):
    return key % 250
