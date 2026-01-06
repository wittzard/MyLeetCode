class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def dfs(state, remaining):
            if len(state) == n:
                result.append(state[:])
                return

            for i in range(len(remaining)):
                num = remaining[i]
                
                state.append(num) # add state
                remaining.pop(i) # remaining must shink

                dfs(state, remaining) # deep-drive ลงสุด จนเจอ base case

                state.pop()
                remaining.insert(i,num)

        dfs([], nums[:])

        return result


    



        