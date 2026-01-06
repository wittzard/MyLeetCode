class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        depth = len(nums)
        result = []
        path = [] # global

        def dfs(i):
            if i == depth:
                result.append(path[:])
                return
            
            # don't pick
            dfs(i+1)

            # pick
            path.append(nums[i]) # เริ่ม i = 3 ก่อน
            dfs(i+1)
            path.pop()

        dfs(0)
        return result
