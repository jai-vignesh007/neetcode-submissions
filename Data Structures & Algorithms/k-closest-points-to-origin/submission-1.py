import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        f=[]
        for x,y in points:
            dis=math.sqrt((pow(x,2))+(pow(y,2)))
            heapq.heappush(res,(dis,[x,y]))
        while k >0:
            dis, point = heapq.heappop(res)
            f.append(point)
            k-=1
        return f

            