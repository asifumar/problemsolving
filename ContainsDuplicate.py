import pdb
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            try:
                d[i] += i:
                return True
            except:
                d[i] = i
            #pdb.set_trace()
        return False

nums = [1,2,3,1]
test = Solution()
print(test.containsDuplicate(nums))