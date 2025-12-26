class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # global
        max_product = nums[0]

        # local
        dp_max = [0]*n
        dp_max[0] = nums[0]
        
        dp_min = [0]*n
        dp_min[0] = nums[0]

        # concept คือ เก็บค่า min มาเพื่อเอามาหาในภายหลัง
        for i in range(1,n):
            x = nums[i]
            
            dp_max[i] = max(x, dp_max[i-1]*x, dp_min[i-1]*x)
            dp_min[i] = min(x, dp_max[i-1]*x, dp_min[i-1]*x)

            max_product = max(dp_max[i], max_product)
            
        return max_product

        def maxProduct(self, nums: List[int]) -> int:
            n = len(nums)

            # global
            max_product = nums[0]
            # local
            max_sofar = nums[0]
            min_sofar = nums[0]

            # concept คือ เก็บค่า min มาเพื่อเอามาหาในภายหลัง
            for i in range(1,n):
                x = nums[i]
                
                max_sofar = max(x, max_sofar*x, min_sofar*x)
                min_sofar = min(x, max_sofar*x, min_sofar*x)

                max_product = max(max_sofar, max_product)
                
            return max_product