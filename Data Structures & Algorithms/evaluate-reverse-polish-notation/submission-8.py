class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operater = {'+', '-', '*', '/'}
        def apply(f,s,o):
            if o == '+':
                return f+s
            if o == '-':
                return f-s
            if o == '*':
                return int(f*s)
            if o == '/':
                return int(f/s)
        cache = []
        for x in tokens:
            if x in operater:
                second = cache.pop()
                first = cache.pop()
                res = apply(first,second,x)
                cache.append(res)
            else:
                cache.append(int(x))
        return cache[-1]

                