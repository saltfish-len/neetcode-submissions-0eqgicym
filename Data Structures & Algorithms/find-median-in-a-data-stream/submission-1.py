class MedianFinder:

    def __init__(self):
        self.less = [] # max heap
        self.more = [] # min heap
        # suppose current medium is less[0]
        # keep len(less) >= len(more)


    def addNum(self, num: int) -> None:
        if len(self.less) == 0:
            heapq.heappush(self.less, -num)
            return
        if num < -self.less[0]:
            heapq.heappush(self.less, -num)
        else:
            heapq.heappush(self.more, num)
        
        # balance
        if len(self.less) < len(self.more):
            m = heapq.heappop(self.more)
            heapq.heappush(self.less, -m)
        if len(self.less) > len(self.more)+1:
            m = -heapq.heappop(self.less)
            heapq.heappush(self.more, m)

                

    def findMedian(self) -> float:
        if len(self.less) == len(self.more):
            med = (-self.less[0] + self.more[0])/2
        else:
            med = -self.less[0] 
        return med
        
        