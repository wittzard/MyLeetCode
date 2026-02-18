from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        window_length = 0
        n = len(s)

        l = 0
        for r in range(n):
            window[s[r]] += 1

            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1 

            window_length = max(window_length, r-l+1)
        
        return window_length
            
