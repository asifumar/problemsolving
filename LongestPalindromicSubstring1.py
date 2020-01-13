import pdb
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        pal  = [[0 for i in s] for i in s]

        for i in range(len(s)):
            pal[i][i] = 1

        for cl in range(1,len(s)):
            for i in range(len(s)-cl):
                j = i + cl
                if s[i]==s[j]:
                    if pal[i+1][j-1] == (j-i-1):
                        pal[i][j] = pal[i+1][j-1] + 2
                    else:
                        pal[i][j] = max(pal[i][j-1], pal[i+1][j])
                    
                else:
                    pal[i][j] = max(pal[i][j-1], pal[i+1][j])
        count = pal[0][len(s)-1]
        print(pal)
        for i in range(len(s)):
            if pal[0][i] == count:
                return s[i+1-count:i+1]

s = 'babadada'

test = Solution()
print(test.longestPalindrome(s))