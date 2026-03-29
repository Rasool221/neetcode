import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","/","*"}
        for i in tokens:
            if i in operators:
                rhs = stack.pop()
                lhs = stack.pop()
                result = math.floor(eval(f"{lhs} {i} {rhs}"))
                stack.append(result)
            else:
                stack.append(i)

        return stack.pop()
        

            