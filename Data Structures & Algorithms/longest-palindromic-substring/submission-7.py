class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j]: s[i:j+1] is Palindromic
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]
        res = ''
        for i in reversed(range(n)):
            for j in range(i,n):
                dp[i][j] = s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1])
                if dp[i][j] and j-i+1>len(res):
                    res = s[i:j+1]

        return res