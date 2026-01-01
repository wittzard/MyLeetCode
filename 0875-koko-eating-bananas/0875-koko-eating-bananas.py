import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # boundary of k is 1 <= k <= max(pile)
        def feasible(k):
            total_hours = 0
            for pile in piles:
                total_hours += (k+pile-1) // k # math notation for floor up

            return total_hours <= h

        # use binary search to find first True 
        l = 1
        r = max(piles)
        i = -1 
        while l <= r:
            k = (l+r)//2
            if feasible(k):
                i = k
                r = k - 1
            else:
                l = k + 1
        
        return i




        