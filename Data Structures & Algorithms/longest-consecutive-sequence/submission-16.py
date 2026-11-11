class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums=set(nums)
        ml=0

        for n in snums:
            l=1
            if n-1 not in snums:
                while n+1 in snums:
                    l+=1
                    n=n+1
            ml=max(l,ml)
        return ml
        