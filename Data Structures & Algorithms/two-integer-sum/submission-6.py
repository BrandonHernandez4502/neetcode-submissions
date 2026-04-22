class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        i = 0
        curr = 0
        n = len(nums)
        count = 0
        while i <= n - 1:
            if nums[curr] + nums[i + 1] == target:
                solution.append(curr)
                solution.append(i + 1)
                return solution
            if i == n - 2:
                count += 1
                i = count
                curr = i
                continue;
            i += 1
        return solution