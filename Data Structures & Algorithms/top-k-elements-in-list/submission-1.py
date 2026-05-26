class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frq=[[]for i in range(len(nums)+1)]
        for i in nums:
            count[i]=count.get(i,0)+1
        for num,cnt in count.items():
            frq[cnt].append(num)
        res=[]
        for num in range(len(frq)-1,0,-1):
            for j in frq[num]:
                res.append(j)
                if len(res)==k:
                    return res







            

        


        