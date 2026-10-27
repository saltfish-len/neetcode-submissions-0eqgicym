class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = 0
        laste = intervals[0][1]
        for s, e in intervals[1:]:
            if laste <= s:
                # no overlap
                laste = e
            else:
                laste = min(laste, e)
                res += 1
        return res
