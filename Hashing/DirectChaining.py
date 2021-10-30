# Direct Chaining Collision Resolution Technique


class HashTable:
    def __init__(self):
        self.hashsize = 10
        self.hashtable = [[] for _ in range(self.hashsize)]

    def get_hash_key(self, key):
        total = 0
        for i in key:
            total += ord(i)
        return total % self.hashsize


    def __setitem__(self, key, value):
        h = self.get_hash_key(key)
    
        # if the key is same
        for index, element in enumerate(self.hashtable[h]):
            if element[0] == key:
                self.hashtable[h][index] = (key, value)
                return 
        # append colloded element in a list
        self.hashtable[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash_key(key)
        for index in self.hashtable[h]:
            if index[0] == key:
                return index[1]

    def __delitem__(self, key):
        h = self.get_hash_key(key)
        for index, element in enumerate(self.hashtable[h]):
            if element[0] == key:
                del self.hashtable[h][index]

t = HashTable()
t['march 6'] = 120
t['march 6'] = 145
t['march 6'] = 1450
t['march 6'] = 14500


t['march 7'] = 500
t['march 8'] = 150
t['march 17'] = 15000



print(t.hashtable)

print(t['march 8'])

del t['march 7']
print(t.hashtable)
