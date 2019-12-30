import pdb
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = 1 + len(nums)//2
        d = {}

        for i in nums:
            #pdb.set_trace()
            if d.get(i):
                d[i] += 1

                if d[i] >= length:
                    return i
            else:
                d[i] = 1
        return nums[0]
l = [2,2,1,1,1,2,2]
test = Solution()
print(test.majorityElement(l))
