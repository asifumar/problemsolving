from typing import List
class Solution:
    def unorderedSearch(self, nums: List[int], l, r, target: int):

        if l<= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                if nums[mid] > nums[r]:
                    return self.unorderedSearch(nums, mid +1,r, target)
                else:
                    if target<= nums[r]:
                        return self.unorderedSearch(nums, mid +1,r, target)
                    else:
                        return self.unorderedSearch(nums, l, mid-1, target)
            else:
                if nums[mid] < nums[l]:
                    return self.unorderedSearch(nums, l, mid-1, target)
                else:
                    if target>= nums[l]:
                        return self.unorderedSearch(nums, l, mid-1, target)
                    else:
                        return self.unorderedSearch(nums, mid+1, r, target)
        else:
            return -1


    def search(self, nums: List[int], target: int) -> int:
        return self.unorderedSearch(nums, 0, len(nums) -1, target)

nums =[4,5,6,7,0,1,2]
test = Solution()
print(test.search(nums, 3))

