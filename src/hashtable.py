# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """

        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.
        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)
        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        Fill this in.
        """

        # Hash the key and set it to index
        idx = self._hash_mod(key)
        curr_pair = self.storage[idx]

        # Check if there is already a value at that index
        if curr_pair is not None:
            # Overwrite value if key matches
            if curr_pair.key == key:
                curr_pair.value = value
            else:
                # Loop until we found a key match or curr_pair -> None
                while curr_pair is not None:
                    if curr_pair.key == key:
                        curr_pair.value = value
                        break

                    if curr_pair.next is None:
                        curr_pair.next = LinkedPair(key, value)
                    else:
                        curr_pair = curr_pair.next
        else:
            # Give that inex in storage a value
            self.storage[idx] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        """

        # Hash the key
        idx = self._hash_mod(key)
        curr_pair = self.storage[idx]

        # Check if value is stored at given key
        if curr_pair is not None and curr_pair.key is key:

            # If found, remove it
            removed_pair = curr_pair
            self.storage[idx] = None

            return removed_pair.value

        if curr_pair is not None and curr_pair.next is not None:
            # Loop thru linked list for key to retrieve pair to remove
            while curr_pair is not None:
                if curr_pair.key == key:
                    removed_pair = curr_pair
                    self.storage[idx] = None

                    return removed_pair.value
                else:
                    curr_pair = curr_pair.next
        else:
            return None

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        """

        idx = self._hash_mod(key)
        curr_pair = self.storage[idx]

        # Check if value is stored at given key
        if curr_pair is not None and curr_pair.key is key:
            # Retrieve value and return it
            found = curr_pair
            return found.value

        elif curr_pair is not None:
            # Loop thru linked list for key to retrieve
            while curr_pair is not None:
                if curr_pair.key == key:
                    found = curr_pair
                    return found.value
                else:
                    curr_pair = curr_pair.next
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        """

        # Double capacity
        self.capacity *= 2
        new_storage = HashTable(self.capacity)

        # Rehash all key/value pairs
        # Traverse thru self.storage
        for pair in self.storage:
            if pair is not None:
                # And insert each pair into new storage
                new_storage.insert(pair.key, pair.value)

            if pair is not None and pair.next is not None:
                curr = pair.next
                while curr is not None:
                    new_storage.insert(curr.key, curr.value)
                    curr = curr.next

        self.storage = new_storage.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_3", "It's working")

    print("")
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
