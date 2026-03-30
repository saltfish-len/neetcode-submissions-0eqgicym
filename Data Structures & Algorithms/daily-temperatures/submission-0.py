class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack
        # if increasing, pop and assign number
        # if decreasing, push
        # it is monotonic as one increasing, as we pop all element smaller than cur
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                # first element
                stack.append((t, i))
                continue
            # compare cur with top
            prev = stack[-1]
            while prev[0] < t:
                # set prev res to cur
                stack.pop()
                res[prev[1]] = i-prev[1]
                if stack:
                    prev = stack[-1]
                else:
                    break

            # now top >= cur, push safely
            stack.append((t, i))
        
        return res



