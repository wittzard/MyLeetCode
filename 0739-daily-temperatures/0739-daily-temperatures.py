class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n

        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                i_top, t_top = stack.pop()
                result[i_top] = i - i_top
            
            stack.append((i,t))
        
        return result
