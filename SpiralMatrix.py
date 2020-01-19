from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix[0]), len(matrix)
        visited = [[False for i in range(m)] for j in range(n)]
        result = []
        step = 'right'
        i, j = 0, 0

        def traverse(matrix, i, j, step):
            if i>=0 and i<n and j>=0 and j<m and visited[i][j]==False:
                visited[i][j]=True
                result.append(matrix[i][j])

                if step=='right':
                    traverse(matrix, i, j+1, step)
                    traverse(matrix, i+1, j, 'down')

                elif step=='down':
                    traverse(matrix, i+1, j, step)
                    traverse(matrix, i, j-1, 'left')
                elif step=='left':
                    traverse(matrix, i, j-1, step)
                    traverse(matrix, i-1, j, 'up')
                else:
                    traverse(matrix, i-1, j, step)
                    traverse(matrix, i, j+1, 'right')
            else:
                return

        traverse(matrix, i , j, step)
        print(visited)

        return result

nums = [[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]

test = Solution()
print(test.spiralOrder(nums))