import pdb
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            else:
                while l<r:
                    total = nums[i] + nums[l] + nums[r]
                    if total>0:
                        r -= 1
                    elif total<0:
                        l += 1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l += 1
                        while l<r and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1

        return triplets

nums  = [-1, 0, 1, 2, -1, -4]
test = Solution()
print(test.threeSum(nums))


