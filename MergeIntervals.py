from typing import List
#author: Umar
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        i = 0

        #breakpoint()
        while i<len(intervals)-1:
            if intervals[i+1][0]<=intervals[i][1]:
                intervals.insert(i, [intervals[i][0], max(intervals[i][1], intervals[i+1][1])])
                intervals.pop(i+1)
                intervals.pop(i+1)
            else:
                i += 1
        return intervals


nums = [[4,5],[1,4]]

test = Solution()
print(test.merge(nums))