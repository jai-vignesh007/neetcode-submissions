class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)

        for n in nums:
            if count[n]<2:
                continue
            
            new_count=defaultdict(int)

            for i,c in nums.items():
                if c > 1:
                    new_count[i]=c-1
            count=new_count
        
        res=[]
        for n in count:
            if nums.count(n)>len(nums)//3:
                res.append(n)
        return res
