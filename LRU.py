class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.age_t = {}
        self.age = -1

    def get(self, key: int) -> int:

        if key in self.d:
            self.age+=1
            self.age_t[key] = self.age
            return self.d[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:

        self.age+=1

        if self.capacity > 0:
            if key in self.d:
                return
            self.d[key] = value
            self.age_t[key] = self.age
            self.capacity-=1

        else:  
            min_key = min(self.age_t, key = self.age_t.get)
            del self.age_t[min_key]
            del self.d[min_key]

            if key in self.d:
                return
            self.d[key] = value
            self.age_t[key] = self.age


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
obj.put(2,1)
obj.put(2, 2)


print(obj.d)
print(obj.age_t)