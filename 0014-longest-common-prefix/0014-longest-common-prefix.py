class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_length = min([len(string) for string in strs])
        for i in range(min_length):
            for j in range(len(strs)):
                if strs[j][i]!=strs[0][i]:
                    return prefix
            prefix = prefix+strs[0][i]
        return prefix