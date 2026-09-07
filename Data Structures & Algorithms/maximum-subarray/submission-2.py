class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            if curmax<0:
                curmax=0
            curmax+=nums[i]
            maxsum=max(curmax,maxsum)
        return maxsum

        
        