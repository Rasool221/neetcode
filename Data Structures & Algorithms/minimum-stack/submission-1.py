class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_top = self.get_min_top()
        if min_top is None or val <= min_top:
            self.min_stack.append(val)

    def pop(self) -> None:
        top_element = self.top()
        min_top_element = self.get_min_top()
        if top_element == min_top_element:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.get_min_top()

    def get_min_top(self) -> int | None:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[len(self.min_stack) - 1] 
