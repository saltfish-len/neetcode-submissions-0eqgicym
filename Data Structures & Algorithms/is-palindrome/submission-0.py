class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = ""
        for x in s:
            if ord('0') <= ord(x) <= ord('9') or \
               ord('A') <= ord(x) <= ord('Z') or \
               ord('a') <= ord(x) <= ord('z'):
                alph+=x.lower()

        n = len(alph)
        for i in range(n):
            if alph[i] != alph[n-i-1]:
                return False
        return True

