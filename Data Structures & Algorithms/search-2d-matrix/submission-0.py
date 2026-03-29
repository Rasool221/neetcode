# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# iteration 0: pick midpoint of m which is index 1
    # [10,11,12,13]
    # check lower and upper bounds
        # if they're target, return true
        # if they're not, check if target is within, if it is, do bin search
        # if not, pull out, and depending on where target is relative to m, do bin search
        # on upper or lower sides

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin(arr: list[int]) -> bool:
            upper = len(arr) - 1
            lower = 0

            while upper - lower != 0 and lower < upper:
                mid = (upper + lower) // 2
                if target > arr[mid]:
                    lower = mid + 1
                elif target < arr[mid]:
                    upper = mid - 1
                else:
                    return True
            
            return False

        upper = len(matrix) - 1
        lower = 0

        while upper - lower != 0 and lower < upper:
            mid = (upper + lower) // 2
            mid_arr = matrix[mid]

            lower_of_mid = mid_arr[0]
            upper_of_mid = mid_arr[len(mid_arr)-1]

            if target in (lower_of_mid, upper_of_mid):
                return True

            if target > upper_of_mid:
                lower = mid + 1
            elif target < lower_of_mid:
                upper = mid - 1
            else:
                return bin(mid_arr)

        return bin(matrix[lower])

