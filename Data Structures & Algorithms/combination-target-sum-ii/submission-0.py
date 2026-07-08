class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        
        def dfs(i,t,subset):
            if t==target:
                res.append(subset.copy())
                return
            if i>=len(nums) or t>target:
                return
            
            subset.append(nums[i])
            dfs(i+1,t+nums[i],subset)

            while i +1 <len(nums) and nums[i]==nums[i+1]:
                i+=1

            subset.pop()
            dfs(i+1,t,subset)
        dfs(0,0,[])
        return res
        
        