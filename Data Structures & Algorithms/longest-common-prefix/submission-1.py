class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        minlen=10000
        for i in strs:
            l=len(i)
            minlen=min(l,minlen)
        for i in range(minlen):
            c=strs[0][i]
            print(c)
            f=0
            for j in range(len(strs)):
                if c!=strs[j][i]:
                    return res
                else:
                    f=1
            if f==1:
                res+=(strs[0][i])
        return res

        