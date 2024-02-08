class Solution:
    def __init__(self):
        self.target_counter = {}
        self.cur_counter = {}
    def satisfy(self) -> bool:
        for key in self.target_counter:
            if not key in self.cur_counter:
                return False
            if self.target_counter[key]>self.cur_counter[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        history_x, history_y = -1, -1
        for letter in t:
            if letter in self.target_counter:
                self.target_counter[letter]+=1
            else:
                self.target_counter[letter] = 1
        left_cur,right_cur = -1, -1
        while right_cur<len(s):
            if self.satisfy():
                if length >= right_cur-left_cur:
                    history_x, history_y = left_cur, right_cur
                length = min(length, right_cur-left_cur)
                left_cur+=1
                self.cur_counter[s[left_cur]]-=1
                if self.cur_counter[s[left_cur]] == 0:
                    del self.cur_counter[s[left_cur]]
            else:
                right_cur+=1
                if right_cur == len(s):
                    if self.satisfy():
                        if length > right_cur-left_cur:
                            history_x, history_y = left_cur, right_cur
                        length = min(length, right_cur-left_cur)
                    break

                if s[right_cur] in self.cur_counter:
                    self.cur_counter[s[right_cur]]+=1
                else:
                    self.cur_counter[s[right_cur]] = 1
        return s[history_x+1:history_y+1]