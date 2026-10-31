class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        minlen=10000
        for i in strs:
            l=len(i)
            minlen=min(l,minlen)
        for i in range(minlen):
            c=strs[0][i]
            for j in range(len(strs)):
                if c!=strs[j][i]:
                    return res
            res+=(strs[0][i])
        return res

        