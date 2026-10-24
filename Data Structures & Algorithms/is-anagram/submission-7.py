class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # v={}
        # for i in range(len(s)):
        #     v[s[i]]+=v.get(s[i],0)+1
        #     v[t[i]]+=t.get(t[i],0)-1
        # for i in v.values():
        #     if i!=0:
        #         return False
        # return True
        t="".join(sorted(t))
        s="".join(sorted(s))
        return t==s
