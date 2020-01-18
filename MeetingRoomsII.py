class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[0])

        l = []
        l.append(intervlas[0][1])
        count = 1

        while i in range(1, len(intervals)):
            if intervals[i][0]<min(l):
                count += 1
                l.append(intervals[i][1])
            else:
                l.remove(min(l))
                l.append(intervals[i][1])
        return count

