"""
MAP Abstract Data Type
Map() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored in the map.
in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
"""
class HashTable(object):
    def __init__(self, size = 11):
        self.size = size
        self.keys = [None] * size # keys
        self.values = [None] * size # values

    def put(self, key, value):
        hashval = self.hash(key)

        if hashval not in keys:
            self.keys[hashval] = key
            self.values[hashval] = value
        else:
            if self.keys[hashval] == key: # replace
                self.values[hashval] = value
            else: # probing
                rehashval = self.rehash(key)
                while self.keys[rehashval] is not None and \
                        self.keys[rehashval] != key:
                    rehashval = self.rehash(rehashval)
                if keys[rehashval] is None:
                    self.keys[rehashval] = key
                    self.values[rehashval] = value
                else:
                    self.values[rehashval] = value # replacee

    def get(self, key):
        pass

    def hash(self, key):
        return key % self.size

    def rehash(self, oldhash):
        """
        linear probing
        """
        return (oldhash + 1) % self.size

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


