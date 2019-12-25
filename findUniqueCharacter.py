import pdb
class Solution:
    def firstUniqChar(self, s: str) -> int:
        self.d = {}

        for i, c in enumerate(s):
            #pdb.set_trace()
            if c in self.d.keys():
                self.d[c] = -1
            else:
                self.d[c] = i
            print(self.d.keys())


        for c in s:
            if self.d[c] != -1:
                return self.d[c]

test = Solution()
s = 'mbafmfxp'
print(test.firstUniqChar(s))
