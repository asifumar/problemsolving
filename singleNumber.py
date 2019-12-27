from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d.keys():
                del d[i]
            else:
                d[i] = 1
        #t = list(d.keys())
        return d.popitem()[0]

test = Solution()
d = [4,1,2,1,2]
res = test.singleNumber(d)
print(type(res))