class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they are anagrams of each other
        
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


        