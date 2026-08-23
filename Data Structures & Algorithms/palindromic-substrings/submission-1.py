class Solution:
    def countSubstrings(self, s: str) -> int:

        res = ""
        reslen = 0
        c=0

        for i in range(len(s)):
            # Check odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c+=1
                
                l -= 1
                r += 1
            
            # Check even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c+=1
                l -= 1
                r += 1
            
        # Unindented to run after the loop completes
        return c