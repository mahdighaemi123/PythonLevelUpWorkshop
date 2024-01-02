# A hash function is a mathematical function that takes an input (or "message") and produces a fixed-size string of bytes. This output string is typically a hash value or hash code.

# solution 1
import hashlib

# install hashlib: pip install hashlib

def sha256_hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


my_data = "ABC"
print(sha256_hash(my_data))


# solution 2 (dont use)
my_data = "ABC"
print(hash(my_data))  # will change with each python run
print(hash(my_data))  # will change with each python run
