#Author: Umar
class Solution:
    def isPalindrome(self, s: str) -> bool:
        whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        s = ''.join(filter(whitelist.__contains__, s))
        self.temp = s.lower()
        self.temp2 = self.temp[::-1]

        if self.temp==self.temp2:
            return True
        else:
            return False

s = ""
test = Solution()
print(test.isPalindrome(s))

