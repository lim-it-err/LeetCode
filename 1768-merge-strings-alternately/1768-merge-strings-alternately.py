class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        i, j = len(word1), len(word2)
        for k in range(max(i, j)):
            if k < i:
                answer += word1[k]
            if k < j:
                answer += word2[k]
        return answer
