class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 0
        product_arr = []
        visited = []
        res = []
        while curr < len(nums):
            product_arr.extend(visited)
            product_arr.extend(nums[curr + 1: len(nums)])
            res.append(math.prod(product_arr))
            visited.append(nums[curr])
            product_arr.clear()
            curr += 1
        return res
