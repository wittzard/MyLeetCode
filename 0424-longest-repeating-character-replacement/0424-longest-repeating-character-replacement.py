class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = {}
        n = len(s)
        optimal = 0
        max_freq = 0

        l = 0 
        for r in range(n):
            memo[s[r]] = memo.get(s[r], 0) + 1
            max_freq = max(max_freq, memo[s[r]])

            while (r-l+1) - max_freq > k:
                memo[s[l]] -= 1
                l += 1

            optimal = max(optimal, r-l+1)

        return optimal

        