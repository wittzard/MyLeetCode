from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = defaultdict(int)
        for num in nums:
            if num in memo:
                return True
            else:
                memo[num] +=1
        return False
    