class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in the table."""
        bucket_index = self.calculate_hash_value(string)
        head = self.table[bucket_index]
        if head is None:
            head = []
        head.append(string)
        self.table[bucket_index] = head

    def lookup(self, string):
        """Return the hash value if the string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        head = self.table[hash_value]
        if head and string in head:
            return hash_value
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a hash value from a string."""
        first_char = string[0]
        second_char = string[1]
        hash_value = ord(first_char) * 100 + ord(second_char)
        return hash_value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
