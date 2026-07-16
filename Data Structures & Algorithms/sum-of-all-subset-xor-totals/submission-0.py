class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,t):
            if i==len(nums):
                return t
            
            return dfs(i+1,t^nums[i])+dfs(i+1,t)
        return dfs(0,0)
        