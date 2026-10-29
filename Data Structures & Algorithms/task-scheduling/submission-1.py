class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # do the most tasks
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1
        
        h = [] # available task sorted by freq
        for k,v in count.items():
            heapq.heappush(h, (-v,k)) # -freq, task
        cooldown = [] # next available time
        time = 0
        while h or cooldown:
            # update available task
            if cooldown and time > cooldown[0][0]:
                heapq.heappush(h, cooldown.pop(0)[1])

            if h:
                v, t = heapq.heappop(h)
                # assign it at time
                if -v > 1: # not the last
                    nextTime = time + n
                    cooldown.append((nextTime, (v+1, t)))
            # time update
            time += 1
            
        return time

        
