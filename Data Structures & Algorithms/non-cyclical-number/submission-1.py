class Solution:
    def isHappy(self, n: int) -> bool:
        # use a set to store viewed numbers
        seen = set()
        def getSum(x:int)->int:
            return int(sum([int(digit)**2 for digit in str(x)]))
        if n == 1: return True
        x = n
        while x not in seen:
            seen.add(x)
            x = getSum(x)
            if x == 1: return True
            
        return False