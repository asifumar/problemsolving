from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, i in enumerate(nums):
            dict[i] = index

        print(dict)
        for i in nums:
            target_val = target - i

            if target_val in dict:
                print(dict[i], "  ", dict[target_val])


nums = [3, 3]
test = Solution()
test.twoSum(nums, 6)

