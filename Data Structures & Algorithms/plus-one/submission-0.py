class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        addone = True
        i = n-1
        while addone and i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i-=1
            else:
                digits[i]+=1
                addone = False
                return digits
        if addone:
            return [1]+digits