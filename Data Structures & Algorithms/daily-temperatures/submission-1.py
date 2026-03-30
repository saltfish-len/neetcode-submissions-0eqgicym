class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack
        # if increasing, pop and assign number
        # if decreasing, push
        # it is monotonic as one increasing, as we pop all element smaller than cur
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
  
            while stack and stack[-1][0] < t:
                # set prev res to cur
                prev = stack.pop()
                res[prev[1]] = i-prev[1]

            # now top >= cur, push safely
            stack.append((t, i))
        
        return res



