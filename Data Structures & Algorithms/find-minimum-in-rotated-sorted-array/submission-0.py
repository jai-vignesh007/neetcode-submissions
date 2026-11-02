class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]>nums[r]:
                l+=1
            elif nums[l]<nums[r]:
                r-=1
            else:
                return nums[l]

        