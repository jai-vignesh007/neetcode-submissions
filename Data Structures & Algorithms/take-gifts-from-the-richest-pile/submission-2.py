import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-g for g in gifts]
        heapq.heapify(gifts)
        t=0
        while k>0:
            k-=1
            gif=heapq.heappop(gifts)
            p=math.sqrt((abs(gif)))
            p=math.floor(p)
            heapq.heappush(gifts,-p)
        return -1*sum(gifts)