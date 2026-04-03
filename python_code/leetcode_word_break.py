# Problem: Leetcode.com
# https://leetcode.com/problems/word-break/description/
# See Gmail Apr 2, 2026, 7:30 AM from Instabyte.io - Subject: "Oracle Lays Off 30,000"

class WordBreak:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]
