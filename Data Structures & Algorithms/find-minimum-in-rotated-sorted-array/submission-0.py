class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        l = 0
        r = len(nums) - 1
        res = 1000
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l += mid + 1
            elif nums[mid] < nums[l]:
                r-= mid + 1
            
            if nums[mid] < res:
                res = nums[mid]