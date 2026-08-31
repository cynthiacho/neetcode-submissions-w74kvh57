class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = sum(1 for x in arr if x + 1 in hash_set)
        return count