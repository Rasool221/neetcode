class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            left_ptr = numbers[left]
            right_ptr = numbers[right]

            if left_ptr + right_ptr == target:
                break

            if left_ptr + right_ptr > target:
                right -= 1            
            
            if left_ptr + right_ptr < target:
                left += 1 

        return [left + 1, right + 1]