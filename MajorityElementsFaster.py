from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = 1 + len(nums)//2
        d = {}

        for i in nums:
            try:
                d[i] += 1
                if d[i] >= length:
                    return i
            except:
                d[i] = 1
        return nums[0]