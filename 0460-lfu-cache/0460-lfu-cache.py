from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.key_level = {k: 0 for k in range(100001)}
        self.level_key = defaultdict(OrderedDict)
        self.key_value = {}
        self.len = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not self._is_key_valid(key):
            return -1
        level = self.key_level[key]
        del self.level_key[level][key]
        if not self.level_key[level]:
            del self.level_key[level]
        self.level_key[level+1][key] = True
        self.key_level[key] = level+1
        return self.key_value[key]

    def put(self, key: int, value: int) -> None:
        if self._is_key_valid(key):
            self._replace(key, value)
        else:
            self._put_new(key, value)

         
    def _is_key_valid(self, key):
        return self.key_level[key]>0
    def _put_new(self, key, value):
        if self.len == self.capacity:
            min_frequent = min(self.level_key.keys())
            pop_key = next(iter(self.level_key[min_frequent]))
            del self.level_key[min_frequent][pop_key]
            if len(self.level_key[min_frequent])==0:
                del self.level_key[min_frequent]
            self.key_level[pop_key] = 0 #Deactivate

            self.len-=1
        self.level_key[1][key] = True
        self.key_level[key] = 1
        self.key_value[key] = value
        self.len+=1

    def _replace(self, key, value):
        level = self.key_level[key]
        del self.level_key[level][key]
        if len(self.level_key[level])==0:
            del self.level_key[level]
        self.level_key[level+1][key] = True
        self.key_level[key] = level+1
        self.key_value[key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)