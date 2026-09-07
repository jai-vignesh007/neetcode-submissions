class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nf=0
        nt=0
        for i in bills:
            change=0
            if i==5:
                nf+=1
            if i==10:
                nt+=1
            
            if i>5:
                change=i-5
                if change==15:
                    if nt>0:
                        nt-=1
                        change-=10
                    elif nf>=3:
                        nf-=3
                        change-=15
                # if change==10:
                #     if nt>0:
                #         nt-=1
                #         change-=10
                #     elif nf>2:
                #         nf-=2
                #         change-=10
                if change==5:
                    if nf>0:
                        nf-=1
                        change-=5
            if change!=0:
                return False
        return True

        