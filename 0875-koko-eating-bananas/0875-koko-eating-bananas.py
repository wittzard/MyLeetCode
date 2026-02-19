import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search form min to max eating speed 
        # choose first min that satisfy constraint
        min_speed = 1
        max_speed = max(piles)

        def check(mid):
            total_hours = 0 
            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                return True

            return False

        # use binary search
        l = min_speed
        r = max_speed
        k = -1 
        while l <= r:
            mid = (l+r)//2
            if check(mid): # if true
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return k
            