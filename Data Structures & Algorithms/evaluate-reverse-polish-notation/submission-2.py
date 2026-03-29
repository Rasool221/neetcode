class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","/","*"}
        for i in tokens:
            if i in operators:
                rhs = stack.pop()
                lhs = stack.pop()

                if i == "/":
                    result = eval(f"int({lhs} / {rhs})")
                else:
                    result = eval(f"({lhs}) {i} ({rhs})")

                stack.append(result)
            else:
                stack.append(i)

        return stack.pop()
        

            