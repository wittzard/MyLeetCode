class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        result = []

        min_diff = float('inf')
        for i in range(1,n):
            diff = arr[i] - arr[i-1]
            min_diff = min(diff, min_diff)

        for i in range(1,n):
            diff = arr[i] - arr[i-1]
            if diff == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result
