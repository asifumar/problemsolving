from typing import List
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        board1 = copy.deepcopy(board)
        m = len(board)
        n = len(board[0])
        count = 0

        for i in range(m):
            for j in range(n):
                for a in range(i-1, i+2):
                    for b in range(j-1, j+2):
                        if a>=0 and a<m and b>=0 and b<n and board1[a][b] == 1:
                            count += 1
                
                if board1[i][j] == 1:
                    count -= 1
                    if count <2 or count>3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1
                count = 0


nums = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
test = Solution()
print(test.gameOfLife(nums))
print(nums)