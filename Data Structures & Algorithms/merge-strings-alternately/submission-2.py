class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=len(word1),len(word2)
        l=max(l1,l2)
        res=""
        for i in range(l):
            if i<l1:
                res+=word1[i]
            if i<l2:
                res+=word2[i]
        return res
        
        


        