class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        res = list(s)
        vowels = 'aeiouAEIOU'
        
        while l < r:
            if res[l] not in vowels:
                l += 1
            elif res[r] not in vowels:
                r -= 1
            else:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
        
        return "".join(res)

        