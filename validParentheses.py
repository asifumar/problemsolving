import pdb
class Solution:
    def isValid(self, s: str) -> bool:
        self.l=[]
        if not s:
            return True
        if len(s)%2==1:
            return False
        
        for i in s:
            #pdb.set_trace()
            if not self.l:
                self.l.append(i)
            else:
                curr = self.l[-1]
                
                if curr=='(':
                    if i==')':
                        del self.l[-1]
                    else:
                        self.l.append(i)
                elif curr=='{':
                    if i=='}':
                        del self.l[-1]
                    else:
                        self.l.append(i)
                elif curr=='[':
                    if i==']':
                        del self.l[-1]
                    else:
                        self.l.append(i)
                else:
                    return False
        
        if not self.l:
            return True
        else:
            return False

test = Solution()
print(test.isValid('[]({)}'))