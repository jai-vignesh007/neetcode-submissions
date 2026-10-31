class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={v:i for i,v in enumerate(nums)}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in dic  and dic[diff]!=i:
                return [i,dic[diff]]

        