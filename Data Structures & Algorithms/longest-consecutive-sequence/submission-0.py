

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        res = 0
        current = 0
        start, end = nums[0], nums[-1]
        for i in range(start, end + 1):
            if d.get(i, 0) > 0:
                current += 1
                res = max(res, current)
            else:
                current = 0

        return res
