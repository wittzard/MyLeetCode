class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        from collections import defaultdict
        dd = defaultdict(int)
        lenght = len(cards)+1
        l = 0
        for r in range(len(cards)):
            dd[cards[r]] += 1
            while dd[cards[r]] == 2:
                lenght = min(lenght,r-l+1)
                dd[cards[l]] -= 1 
                l += 1
                
        return lenght if lenght != len(cards)+1 else -1