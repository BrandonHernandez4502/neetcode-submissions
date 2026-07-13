class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_list = []
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][-1] > target:
                bottom = row -1
            else:
                target_row = matrix[row]
                break

        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                target_list = matrix[i]
                break

        l = 0
        r = len(target_list) - 1

        while r >= l:
            mid = (r + l) // 2
            if target_list[mid] > target:
                r = mid - 1
            elif target_list[mid] < target:
                l = mid + 1
            else:
                return True
        return False