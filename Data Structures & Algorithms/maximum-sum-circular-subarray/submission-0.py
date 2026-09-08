class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glmax,glmin=nums[0],nums[0]
        curmax,curmin=0,0
        t=0
        for n in nums:
            curmax=max(curmax+n,n)
            curmin=min(curmin+n,n)
            t+=n
            glmax=max(glmax,curmax)
            glmin=min(glmin,curmin)
        
        return max(glmax,t-glmin) if glmax>0 else glmax 
        

        