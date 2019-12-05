class Solution:

    def check_pal(self, s: str) -> str:
        rev_s = ''

        for k in s[::-1]:
            rev_s = rev_s + k

        if rev_s == s:
            return s
        else:
            return ''
    
    def longestPalindrome(self, s: str) -> str:

        self.max_pal=''

        if len(s)<=1:
            return s

        else:
            for i, a in enumerate(s):
                for j, b in enumerate(s[::-1]):
                    if a==b:
                        #print(s[i:len(s)-j])
                        pal = self.check_pal(s[i:len(s)-j])
                        if len(pal)>len(self.max_pal):
                            self.max_pal = pal
            return self.max_pal
        

    
#time limit exceeded
test = Solution()
inp = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
#result = test.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
#result = test.check_pal('aaaaa')
print(len(inp))


