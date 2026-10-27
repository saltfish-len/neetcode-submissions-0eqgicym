"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        e = 0
        count = 0
        res = 0
        for s in range(len(starts)):
            if ends[e] > starts[s]:
                # need one room
                count += 1
                res = max(count,res)
                continue
            if ends[e] <= starts[s]:
                # one meeting end
                # count -= 1
                # count += 1 this new meeting
                e += 1
        return res
        
