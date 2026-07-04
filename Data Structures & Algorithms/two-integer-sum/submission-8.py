class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for idx, val  in enumerate(nums):
            d[val] = idx
        print(d)

        for i in range((len(nums))):
            difference = target - nums[i]
            if difference in d and d[difference] != i:
                return[i, d[difference]]
        return []