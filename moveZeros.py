from typing import List
class Solution:
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count,i = 0,0


        while count<len(nums):
            
            if nums[i]!=0:
                i+=1
                count+=1
            else:
                del nums[i]
                nums.append(0)
                count+=1

nums = [1,0,5,0,0,2]
Solution.moveZeroes(nums)
print(nums)