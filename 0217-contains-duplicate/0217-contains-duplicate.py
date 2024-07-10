class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            else:
                hash.add(num)
        return False
        