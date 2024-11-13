class HashMap:
    def __init__(self):
        self.max = 100
        self.arr = [[] for _ in range(self.max)]  
        
    def hash_key(self, val):
        h = 0
        for char in val:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.hash_key(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, val)  
                found = True
                break
        if not found:
            self.arr[h].append((key, val))  

    def __getitem__(self, key):
        h = self.hash_key(key)
        for k, v in self.arr[h]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")  
    def __delitem__(self, key):
        h = self.hash_key(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return
        raise KeyError(f"Key '{key}' not found")  


t = HashMap()
t["ji"] = 130
print(t["ji"]) 

t["abc"] = 456
t["xyz"] = 789
print(t["abc"])  
print(t["xyz"])  

del t["ji"]


try:
    print(t["ji"])
except KeyError as e:
    print(e)  
