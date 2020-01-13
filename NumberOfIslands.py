from typing import List
class Solution:
    def checkAdjacent(self, i, j, m, n, grid: List[List[str]], visited: List[List[bool]]):
        if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j]=='0' or visited[i][j] == True:
            return
        else:
            visited[i][j] = True
            self.checkAdjacent(i, j+1, m, n, grid, visited)
            self.checkAdjacent(i+1, j, m, n, grid, visited)
            self.checkAdjacent(i, j-1, m, n, grid, visited)
            self.checkAdjacent(i-1, j, m, n, grid, visited)
    

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        visited = [[False for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==False:
                    self.checkAdjacent(i, j, m, n, grid, visited)
                    count += 1
        return count


test = Solution()
a = ['11000', '11000', '00100', '00011']
print(test.numIslands(a))