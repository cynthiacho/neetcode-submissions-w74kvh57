class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find the peak index
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak = low

        # 2. Search in the left (ascending) part
        low, high = 0, peak
        while low <= high:
            mid = (low + high) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        # 3. Search in the right (descending) part
        low, high = peak + 1, n - 1
        while low <= high:
            mid = (low + high) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                low = mid + 1
            else:
                high = mid - 1

        return -1