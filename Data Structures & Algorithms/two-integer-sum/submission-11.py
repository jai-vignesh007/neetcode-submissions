class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre={}
        for i,n in enumerate(nums):
            dif=target-n
            if dif in pre:
                return [pre[dif],i]
            pre[n]=i
        