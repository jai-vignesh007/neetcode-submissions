class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr1 = [0] * 27
        arr2 = [0] * 27
        for i in range(0,len(s)):
            arr1[ord(s[i])-96]+=1
        for j in range(0,len(t)):
            arr2[ord(t[j])-96]+=1
        for k in range(0,len(arr1)):
            if arr1[k]!=arr2[k]:
                return False
        return True
       
       
        