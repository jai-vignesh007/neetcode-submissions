class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        para={
            "]":"[",
            ")":"(",
            "}":"{"
        }
        for c in s:
            if c in para:
                if len(stack)!=0 and stack[-1]==para[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack)!=0:
            return False
        else:
            return True







                        