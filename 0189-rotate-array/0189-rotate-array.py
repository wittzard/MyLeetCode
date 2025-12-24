class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # handle case k > n (full-rotate)
        n = len(nums)
        k = k % n 

        swap(0,n-1)
        swap(0,k-1)
        swap(k,n-1)

        return nums
            
        