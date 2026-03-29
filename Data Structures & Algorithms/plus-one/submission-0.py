class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True

        result = digits

        for i in range(len(result)-1, -1, -1):
            if not carry:
                break

            if digits[i] + 1 > 9:
                result[i] = 0
            else:
                result[i] = digits[i] + 1
                carry = False

        if carry:
            return [1] + result
        
        return result
