class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res=[]
            for i in range(4):
                digit=(int(lock[i])+1)%10
                res.append(lock[0:i]+str(digit)+lock[i+1:])
                digit=((int(lock[i])+10)-1)%10
                res.append(lock[0:i]+str(digit)+lock[i+1:])
            return res

        visited=set(deadends)

        q=deque([("0000",0)])
        turn =0
        while q:
            lock,turn=q.popleft()
            if lock == target:
                return turn
            for child in children(lock):
                if child not in visited:
                    q.append([child,turn+1])
                    visited.add(child)
        return -1
