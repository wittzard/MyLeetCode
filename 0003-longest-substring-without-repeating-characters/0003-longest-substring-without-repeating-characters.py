from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_character = defaultdict(int)
        window_lenght = 0

        l = 0
        for r in range(len(s)):
            window_character[s[r]] += 1
            
            # check variant
            while window_character[s[r]] > 1:
                window_character[s[l]] -= 1
                l += 1

            window_lenght = max(window_lenght, r-l+1)

        return window_lenght
                


