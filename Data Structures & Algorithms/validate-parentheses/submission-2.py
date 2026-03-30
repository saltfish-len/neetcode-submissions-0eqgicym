class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bar_map = {'(':')','{':'}','[':']',}
        for bracket in s:
            if bracket in '({[':
                # push 
                stack.append(bracket)
            else:
                # pop
                if len(stack) == 0:
                    return False
                open_bar = stack.pop(-1)
                close_bar = bar_map[open_bar]
                if close_bar != bracket:
                    return False
        
        return len(stack) == 0