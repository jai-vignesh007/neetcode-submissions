class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(l):
            m=i
            for j in range(i+1,l):
                if nums[j]<nums[m]:
                    m=j
            t=nums[i]
            nums[i]=nums[m]
            nums[m]=t

        return nums