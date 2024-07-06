class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        heap = set()
        for i in range(0,len(nums)):
            if nums[i] in heap:
                return nums[i]
            else:
                heap.add(nums[i])
        