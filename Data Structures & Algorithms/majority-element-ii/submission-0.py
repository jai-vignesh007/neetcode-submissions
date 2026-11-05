class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t=len(nums)//3

        d=defaultdict(int)
        res=set()
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>t:
                res.add(i)
        return list(res)

        