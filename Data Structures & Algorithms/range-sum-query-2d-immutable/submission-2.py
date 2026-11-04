class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R=len(matrix)
        C=len(matrix[0])
        self.sumM=[[0]*(C+1) for _ in range(R+1)]
        for i in range(R):
            t=0
            for j in range(C):
                t+=matrix[i][j]
                above=self.sumM[i][j+1]
                self.sumM[i+1][j+1]=t+above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        bottomright=self.sumM[row2][col2]
        above=self.sumM[row1-1][col2]
        left=self.sumM[row2][col1-1]
        topleft=self.sumM[row1-1][col1-1]
        return bottomright-above-left+topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)