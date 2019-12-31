from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []


        l.append([1])
        if numRows == 1:
            return l
        
        l.append([1,1])
        if numRows == 2:
            return l
        for i in range(2, numRows):
            l.append([1])

            for j in range(1,i):
                l[i].append(l[i-1][j-1] + l[i-1][j])

            l[i].append(1)
        return l


test = Solution()
print(test.generate(5))