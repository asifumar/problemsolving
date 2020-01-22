class Solution:
    def numDecodings(self, s: str) -> int:
        l = [0 for i in s]
        l.append(1)
        l[len(s)-1] = 1

        for i in reversed(range(len(s) -1)):
            print(l)
            if int(s[i:i+2])<27:
                l[i] = l[i+1] + l[i+2]
            else:
                l[i] = l[i+1]
        return l[0]



s = "226"
test = Solution()
print(test.numDecodings(s))