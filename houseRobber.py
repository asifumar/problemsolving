from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        listlen = len(nums)
        if listlen==1:
            return nums[0]
        if listlen>2:
            nums[2] += nums[0]

            for i in range(3, listlen):
                nums[i] += max(nums[i-2], nums[i-3])

        return max(nums[listlen-1], nums[listlen-2])

test = Solution()
l = [14,2,7,9,1,10]

print(test.rob(l))