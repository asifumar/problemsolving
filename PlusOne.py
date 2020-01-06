from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        newNum = []
        
        for i in digits:
            total = total*10 + i
        total += 1

        while total !=0:
            newNum.insert(0, total%10)
            total //= 10
        return newNum

digits = [999]

test = Solution()
print(test.plusOne(digits))