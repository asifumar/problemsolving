from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        self.maxways = 0

        for i in range (0, (n//2)+1):
            self.maxways += factorial(n-i)//(factorial(i)*factorial(n-i-i))
            print(self.maxways)

        return self.maxways

test = Solution()
print(test.climbStairs(3))