from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.maxprof = 0
        self.min = prices[0]

        for i in range(len(prices)):
            self.currprofit = prices[i]-self.min
            if self.currprofit>self.maxprof:
                self.maxprof = self.currprofit
            if prices[i]<self.min:
                self.min = prices[i]

        return self.maxprof

prices = [7,2,24,70,11,99,1,80,105]
test = Solution()
print(test.maxProfit(prices))



