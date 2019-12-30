class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxnum = len(nums)    
        return (maxnum*(maxnum+1)//2)-sum(nums)