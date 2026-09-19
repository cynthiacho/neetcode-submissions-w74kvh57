# TWO POINTERS

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        n = len(s)
        count = [0] * n
        s = list(s)
        for j in range(n):
            s[i] = s[j]
            count[i] = 1
            if i > 0 and s[i - 1] == s[j]:
                count[i] += count[i - 1]
            if count[i] == k:
                i -= k
            i += 1
        return ''.join(s[:i])