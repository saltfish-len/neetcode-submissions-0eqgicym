class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((t,i))
                continue
            if t <= stack[-1][0]:
                stack.append((t,i))
                continue
            
            while len(stack) > 0 and t > stack[-1][0]:
                prev, pidx = stack.pop()
                res[pidx] = i-pidx
            stack.append((t,i))
            
        return res