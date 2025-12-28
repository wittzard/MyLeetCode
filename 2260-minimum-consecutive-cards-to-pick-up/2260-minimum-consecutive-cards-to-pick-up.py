from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        lenght = n + 1

        count = defaultdict(int)
        l = 0
        for r in range(n):
            count[cards[r]] += 1

            while count[cards[r]] > 1:
                lenght = min(lenght, r-l+1)
                count[cards[l]] -= 1
                l += 1
        
        if lenght == n + 1:
            return -1

        return lenght

            

        