# BRUTE FORCE

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    res.add(i)
                    break
        return list(res)

# BUILT IN FUNCTIONS

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
            return list(set(nums1) & set(nums2))