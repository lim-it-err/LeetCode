from collections import defaultdict
class AllOne:
    def __init__(self):
        self.value_frequency = {}
        self.frequency_value = defaultdict(dict)

    def inc(self, key: str) -> None:
        if not key in self.value_frequency:
            self._add_new(key)
        cur_freq = self.value_frequency[key]
        del self.frequency_value[cur_freq][key]
        if not self.frequency_value[cur_freq]:
            del self.frequency_value[cur_freq]
        self.frequency_value[cur_freq+1][key] = 1
        self.value_frequency[key]+=1


    def dec(self, key: str) -> None:
        assert key in self.value_frequency, "No key in dec operation"
        cur_freq = self.value_frequency[key]
        del self.frequency_value[cur_freq][key]
        if cur_freq-1>0:
            self.frequency_value[cur_freq-1][key] = 1
        if not self.frequency_value[cur_freq]:
            del self.frequency_value[cur_freq]
        self.value_frequency[key]-=1
        if self.value_frequency[key] == 0:
            del self.value_frequency[key]
        print(self.value_frequency)
        print(self.frequency_value)

    def getMaxKey(self) -> str:
        if not self.frequency_value:
            return ""
        max_frequent = max(self.frequency_value.keys())
        return next(iter(self.frequency_value[max_frequent]))

    def getMinKey(self) -> str:
        if not self.frequency_value:
            return ""

        min_frequent = min(self.frequency_value.keys())
        return next(iter(self.frequency_value[min_frequent]))
            
    def _add_new(self, key):
        self.value_frequency[key] = 0
        self.frequency_value[0][key] = 0

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


1 1 1 2 2 2 3 3 4 4 4 5 5 5 6 -> 1 1 1 3
