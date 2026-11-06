class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        m=1
        for i in nums:
            if i>0 and m==i:
                m+=1
        return m 