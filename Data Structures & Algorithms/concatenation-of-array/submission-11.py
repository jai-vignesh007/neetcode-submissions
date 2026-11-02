class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[0]*(l*2)
        for i in range(l):
            res[i]=nums[i]
            res[i+l]=nums[i]
        return res

        