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

