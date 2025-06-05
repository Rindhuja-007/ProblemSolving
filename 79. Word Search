class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def searchWord(x:int,y:int,index:int)->bool:
            if index==len(word)-1:
                return board[x][y]==word[index]
            if board[x][y]!=word[index]:
                return False
            
            temp=board[x][y]
            board[x][y]="0"

            directions=[(-1,0),(0,1),(1,0),(0,-1)]

            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<row and 0<=ny<col and board[nx][ny]!="0":
                    if searchWord(nx,ny,index+1):
                        return True
            board[x][y]=temp
            return False

        row,col=len(board),len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j]== word[0] and searchWord(i,j,0):
                    return True
        return False
