class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        counter = 1
        best_count = 1
        if not nums:
            return 0
        for i in range(0, len(sorted_nums) - 1):
            if sorted_nums[i+1] - sorted_nums[i] == 0:
                continue;
            elif sorted_nums[i+1] - sorted_nums[i] == 1:
                counter += 1
                if counter > best_count:
                    best_count = counter
            else:
                counter = 1
        return best_count