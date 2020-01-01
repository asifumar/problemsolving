from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 0
        curr = nums[0]

        for num in nums:
            if curr != num:
                curr = num
                index += 1
                nums[index] = num
        return index+1

nums = [1,2,2,3]
test = Solution()
print(test.removeDuplicates(nums))
print(nums)