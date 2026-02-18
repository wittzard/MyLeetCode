class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []

        for i in range(n):
            new_temp = (temperatures[i], i)
            
            # while stack is not null and top is lesser than curr temp
            while stack and stack[-1][0] < new_temp[0]:
                temp, temp_index = stack.pop()
                result[temp_index] = new_temp[1] - temp_index
            
            stack.append(new_temp)

        return result
