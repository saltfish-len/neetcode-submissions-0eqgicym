class TimeMap:

    def __init__(self):
        self.ktv = {} # key:[(t,v)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ktv[key] = self.ktv.get(key,[])
        self.ktv[key].append((timestamp,value)) # it should be increasing

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ktv.keys():
            return ""
        vals = self.ktv[key] # [(t,v)]
        # search for t
        l = 0
        r = len(vals)-1
        mid = (l+r)//2
        if timestamp < vals[l][0]:
            # not existed 
            return ""
        if timestamp >= vals[r][0]:
            return vals[r][1]

        while l+1 < r:
            if vals[mid][0] > timestamp:
                r = mid
            if vals[mid][0] < timestamp:
                l = mid
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            mid = (l+r)//2

        return vals[mid][1]

