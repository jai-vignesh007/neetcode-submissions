class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l=0
        r=1
        maxp=0
        while r<len(p):
            if p[l]<p[r]:
                maxp=max(p[r]-p[l],maxp)
                
            else:
                l=r
            r+=1
        return maxp

        