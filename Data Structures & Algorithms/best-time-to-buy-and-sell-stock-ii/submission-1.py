class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        i,j=0,1
        t=0
        while i<len(prices)-1 and j<len(prices):
            if prices[j]>prices[i]:
                t+=prices[j]-prices[i]
            i+=1
            j+=1
        return t


        