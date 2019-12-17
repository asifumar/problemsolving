import pdb
class Solution:
    def squaredSum(self, d:int) ->int:
        self.l = []
        self.sm=0
        
        #save digits in list
        while(d>0):
            self.nd=d%10
            self.l.append(self.nd)
            d=d//10
        #print(self.l)
        for i in self.l:
            self.sm=self.sm+(i**2)
            
        return self.sm
        
    def isHappy(self, n: int) -> bool:
        while n:
            if n==1:
                return True
            else:
                n=self.squaredSum(n)
                print(n)
            
test = Solution()
test.isHappy(19)