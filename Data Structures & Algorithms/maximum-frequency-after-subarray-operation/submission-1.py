class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cntK = nums.count(k)
        max_gain = 0

        for num in range(1, 51):
            if num == k: continue
            cur = 0
            for x in nums:
                if x == num:
                    cur += 1
                elif x == k:
                    cur -= 1
                if cur < 0:
                    cur = 0
                if cur > max_gain:
                    max_gain = cur

        return cntK + max_gain