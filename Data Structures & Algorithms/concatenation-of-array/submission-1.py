class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[]
        for i in range(0,2*l):
            ans.append(nums[i%l])
        return ans
            
        
        