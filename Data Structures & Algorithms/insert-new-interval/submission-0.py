class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        # first no overlap
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            res.append([intervals[i][0],intervals[i][1]])
            i+=1
        
        # overlap
        newStart, newEnd = newInterval
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(intervals[i][1], newEnd)
            i += 1
        res.append([newStart,newEnd])

        
        return res+intervals[i:]
