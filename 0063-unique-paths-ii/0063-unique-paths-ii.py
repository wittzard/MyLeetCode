class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # rows and columns
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # eage case 
        if obstacleGrid[0][0]:
            return 0

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 # base case 

        for r in range(m):
            for c in range(n):
                # check if can pass ?
                if obstacleGrid[r][c] == 1:
                    dp[r][c] == 0

                # can move
                else:
                    if r > 0:
                        dp[r][c] += dp[r-1][c]

                    if c > 0:
                        dp[r][c] += dp[r][c-1]

        return dp[m-1][n-1]