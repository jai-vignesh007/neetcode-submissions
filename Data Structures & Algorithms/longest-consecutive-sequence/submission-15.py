class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        ml=0
        for i in d:
            if i-1 not in d:
                l=1
                while i+1 in d:
                    l+=1
                    i+=1
                ml=max(l,ml)
            
        return ml