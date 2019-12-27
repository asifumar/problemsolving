from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intrsction = list(set(nums1) & set(nums2))
        returnval = []
        
        d1 = {}
        d2 = {}

        for i in nums1:
            try:
                d1[i] += 1
            except:
                d1[i] = 1
        
        for i in nums2:
            try:
                d2[i] += 1
            except:
                d2[i] = 1

        for i in intrsction:
            minlen = min(d1[i],d2[i])
            for j in range(0,minlen):
                returnval.append(i)
        return returnval
