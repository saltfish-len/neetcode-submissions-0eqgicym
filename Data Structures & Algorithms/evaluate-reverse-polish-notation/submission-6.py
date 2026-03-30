class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def operate(l,r,o):
            if o=='+':
                return l+r
            if o=='-':
                return l-r
            if o=='*':
                return l*r
            if o=='/':
                return int(float(l) / r)   
        # push numbers, pop when operators
        for x in tokens:
            if x in '+-*/':
                n1 = stack.pop() # seconde
                n2 = stack.pop() # first
                stack.append(operate(n2,n1,x))
            else:
                stack.append(int(x))
        return int(stack[0])