# Python Dictionaries are implemented using Hashing

# we have data of stock price day: stock_price



class HashTable:
    def __init__(self):
        self.hashsize = 100
        self.hashtable = self.hashsize * [None]

    def get_hash_key(self, key):
        total = 0
        for i in key:
            total += ord(i)
        return total % self.hashsize


    def __setitem__(self, key, value):
        h = self.get_hash_key(key)
        self.hashtable[h] = value

    def __getitem__(self, key):
        h = self.get_hash_key(key)
        return self.hashtable[h]

    def __delitem__(self, key):
        h = self.get_hash_key(key)
        self.hashtable[h] = None


t = HashTable()

# insert
t['oct 29'] = 320
t['oct 30'] = 322
t['oct 31'] = 340

print(t.hashtable)

# get 
print(t['oct 31'])

# delete
del t['oct 30']

print(t['oct 30'])
