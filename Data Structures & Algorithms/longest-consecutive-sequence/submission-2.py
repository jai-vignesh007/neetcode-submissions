class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        if len(nums)==0:
            return 0
        maxi =1
        p=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                p+=1
            else:p=1
            if maxi<=p:
                maxi=p            
        return maxi
