class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums_rows = len(matrix)
        nums_cols = len(matrix[0])

        for row in range(nums_rows):
            if matrix[row][nums_cols-1] < target:
                continue
            
            l = 0
            r = nums_cols - 1
            while l <= r:
                m = (l+r)//2
                if matrix[row][m] > target:
                    r = m - 1
                elif matrix[row][m] < target:
                    l = m + 1
                else:
                    return True
                    
        return False

        