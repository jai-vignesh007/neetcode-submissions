class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={v:i for i,v in enumerate(nums)}
        for k in range(len(nums)):
            dif=target-nums[k]
            if dic.get(dif) and dic.get(dif)!=k:
                return [k,dic.get(dif)]