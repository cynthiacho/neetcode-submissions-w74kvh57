# SORTING

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1.sort()
        nums2.sort()

        def helper(A, B):
            n, m = len(A), len(B)
            res = []

            j = 0
            prev = float('-inf')
            for num in A:
                if prev == num:
                    continue
                while j < m and B[j] < num:
                    j += 1
                if j == m or B[j] != num:
                    res.append(num)
                prev = num
            return res

        return [helper(nums1, nums2), helper(nums2, nums1)]