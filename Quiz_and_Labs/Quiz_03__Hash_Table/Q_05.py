"""
The above hash function is used for hashing 3-digitphone number area code (about 300 possible values) into table size of 1000. Choose the best statement.

- It will perform well because the hash values range from 0 to 999, matching the table size.
- It will perform poorly because only about 300 of the 1000 buckets will ever be used, leading to wasted space.
- It will never cause collisions because there are fewer area codes than buckets.

"""


def hashFunction(key):
    return key % 1000
