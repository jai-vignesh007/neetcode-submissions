class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def dfs(op,cp):
            if op==cp==n:
                res.append("".join(stack))
                return
            if op<n:
                stack.append("(")
                dfs(op+1,cp)
                stack.pop()
            if cp<op:
                stack.append(")")
                dfs(op,cp+1)
                stack.pop()
        dfs(0,0)
        return res
        