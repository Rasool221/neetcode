# [30,38,30,36,35,40,28]
# iteration 0: [(30, 0)]
# iteration 1: [(30, 0)] -> [(38, 1)] | [1]
# iteration 2: [(38, 1), (30, 2)] | [1]
# iteration 2: [(38, 1), (30, 2)] -> [(38,1)] | [1,]
# 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            n = temperatures[i]
            if len(stack) > 0:
                while len(stack) > 0 and n > stack[len(stack)-1][0]:
                    top = stack[len(stack)-1]
                    answers[top[1]] = i - top[1]
                    stack.pop()
                    
            stack.append((n, i))

            # print(n, stack, answers)

        return answers
