class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D,R=deque(),deque()
        for i,c in enumerate(senate):
            if c=="R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            Rturn=R.popleft()
            Dturn=D.popleft()
            if Rturn<Dturn:
                R.append(Rturn+len(senate))
            else:
                D.append(Dturn+len(senate))
        return "Radiant" if R else "Dire"

        