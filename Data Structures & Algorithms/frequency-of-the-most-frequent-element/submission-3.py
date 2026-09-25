# ADVANCED SLIDING WINDOW

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        res = 1
        for i in range(n):
            l, r = 0, i
            while l <= r:
                m = (l + r) // 2
                curSum = prefix_sum[i + 1] - prefix_sum[m]
                need = (i - m + 1) * nums[i] - curSum
                if need <= k:
                    r = m - 1
                    res = max(res, i - m + 1)
                else:
                    l = m + 1
        return res