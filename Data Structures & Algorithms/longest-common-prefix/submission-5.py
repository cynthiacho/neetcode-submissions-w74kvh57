class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # are the characters in the string?
        #what is the length of char in string

        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0

            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break

                j += 1

            prefix = prefix[:j]
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]      