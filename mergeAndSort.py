from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.temp = nums1[:m]
        nums1 [:] = []
        a = b = 0

        while a<m and b<n:
            if self.temp[a]<=nums2[b]:
                nums1.append(self.temp[a])
                a += 1
            else:
                nums1.append(nums2[b])
                b += 1
        if a>=m:
            while b<n:
                nums1.append(nums2[b])
                b += 1
        if b>=n:
            while a<m:
                nums1.append(self.temp[a])
                a += 1
