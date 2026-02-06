class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []

        min_abs = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            min_abs = min(min_abs, diff)

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_abs:
                result.append([arr[i-1], arr[i]])
        
        return result