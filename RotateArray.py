from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        duplicatenums = []
        length = len(nums)

        for i in range(length):
            duplicatenums.append(nums[(length-k+i)%length])
        nums[:] = duplicatenums


num = [0,1,2,3,4,5,6,7]
test = Solution()
test.rotate(num, 2)
print(num)