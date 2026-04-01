class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        while True:
            flag = True
            for num in nums:
                if missing == num:
                    flag = False
                    break

            if flag:
                return missing
            missing += 1


nums = []

countMap = {}
for num in nums:
    # If countMap does not contain num
    if num not in countMap:
        countMap[num] = 1
    else:
        countMap[num] += 1

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1