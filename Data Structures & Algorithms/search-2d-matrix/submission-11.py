class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_list = []
        top = 0
        bottom = len(matrix) - 1
        rows = -1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row -1
            else:
                break
        target_list = matrix[row]

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