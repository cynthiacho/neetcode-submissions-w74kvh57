# BRUTE FORCE

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = [set(), set()]

        for num1 in nums1:
            found = False
            for num2 in nums2:
                if num1 == num2:
                    found = True
                    break
            if not found:
                res[0].add(num1)

        for num2 in nums2:
            found = False
            for num1 in nums1:
                if num1 == num2:
                    found = True
                    break
            if not found:
                res[1].add(num2)

        return [list(res[0]), list(res[1])]
