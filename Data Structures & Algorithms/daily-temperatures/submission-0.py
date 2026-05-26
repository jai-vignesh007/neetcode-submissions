class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i  in range(0,len(temperatures)):
            count=0
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    count=j-i
                    break
            result.append(count)
            count=0

        return result
        
        