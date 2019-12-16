#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Solution:
    def reverse(self, x: int) -> int:
        self.l = []
        self.s = 0
        self.rev = 0
        self.p = 0
        
        if x<0:
            x*=-1
            self.s = 1
        
        while x!=0:
            self.l.append(x%10)
            x=x//10
        print(self.l)
        
        for i in self.l[::-1]:
            #print(i)
            self.rev+=(i*(10**self.p))
            self.p+=1
            print(self.rev)
        
        if self.rev<(-2**31) or self.rev>((2**31)-1):
            return 0
        elif self.s==1:
            return self.rev*(-1)
        else:
            return self.rev
            

test=Solution()
test.reverse((2**31)-1)


# In[ ]:




