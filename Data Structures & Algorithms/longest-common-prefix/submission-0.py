class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        l=min(len(s) for s in strs)
        for i in range(l):
            f=0
            for j in range(len(strs)):
                if strs[0][i]!=strs[j][i]:
                    f=1
                    break
            if f==0:
                ans.append(strs[0][i])
            else:
                break
        return "".join(ans)