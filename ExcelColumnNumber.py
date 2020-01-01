import string
class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {}
        temp = 0

        for i in range(26):
            d[string.ascii_uppercase[i]] = i+1
        for char in s:
            temp = temp*26 + d[char]

        return temp

test = Solution()
print(test.titleToNumber("ZY"))