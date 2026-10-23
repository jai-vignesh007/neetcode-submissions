class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<1:
            return False
        nums.sort()
        prev=nums[0]
        for i in range(1,len(nums)):
            if prev==nums[i]:
                return True
            prev=nums[i]
        return False
        
        