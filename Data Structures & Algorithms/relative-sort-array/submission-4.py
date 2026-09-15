# COUNTING SORT

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_val = max(arr1)
        count = [0] * (max_val + 1)

        for num in arr1:
            count[num] += 1

        res = []
        for num in arr2:
            res += [num] * count[num]
            count[num] = 0

        for num in range(len(count)):
            res += [num] * count[num]

        return res

# CUSTOM SORT

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (index.get(x, 1000 + x)))