def alpha_to_num(alphabet):
    return ord(alphabet)-ord("a")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = {}
        self.is_end = False

    def add(self, target):
        data_num = alpha_to_num(target)
        self.next[data_num] = Node(data=target)

    def get(self, target):
        data_num = alpha_to_num(target)
        if not data_num in self.next:
            return None
        return self.next[data_num]
    def exist(self, target) -> bool:
        return alpha_to_num(target) in self.next


class Trie:

    def __init__(self):
        self.head = Node(data = None)

    def insert(self, word: str) -> None:
        cur_node = self.head
        for letter in word:
            if cur_node.exist(letter):
                cur_node = cur_node.get(letter)
                continue
            cur_node.add(letter)
            cur_node = cur_node.get(letter)
        cur_node.is_end = True

    def search(self, word: str) -> bool:
        cur_node = self.head
        for letter in word:
            if not cur_node.exist(letter):
                return False
            cur_node = cur_node.get(letter)
        if cur_node.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.head
        for letter in prefix:
            if not cur_node.exist(letter):
                return False
            cur_node = cur_node.get(letter)
        return True





# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


