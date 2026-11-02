class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            chlist=[0]*26
            for c in s:
                chlist[ord(c)-ord('a')]+=1
            res[tuple(chlist)].append(s)
        return list(res.values())
        