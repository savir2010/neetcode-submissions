class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        if m == 1 and n ==1:
            return matrix[0][0] == target

        start_row = (n+1)//2
        start_col = (m+1)//2
        not_found_row = True
        not_found_col = True
        row = None
        col = None
        prev = -1
        if n == 1:
            row = 0
            not_found_row = False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while not_found_row:
            print(start_row)
            first_r= matrix[start_row][0]
            end_r = matrix[start_row][-1]
            prev = start_row
            if target <= end_r and target >= first_r:
                row = start_row
                not_found_row = False
                break
            elif target <= first_r:
                start_row = (start_row)//2
            elif target >= end_r:
                start_row = start_row + (start_row)//2
            if prev == start_row:
                return False
        
        print(row)
        if m == 1:
            return matrix[row][0] == target
        while not_found_col:
            target_s= matrix[row][start_col]
            prev = start_col
            if target < target_s:
                start_col = (start_col)//2
            elif target > target_s:
                start_col = start_col + (start_col)//2
            elif target == target_s:
                col = start_col
                not_found_col = False
                return True
            if prev == start_col:
                return False
        return False
        