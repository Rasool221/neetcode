# at every decision tree node, you must 
# decide if you're going to open a new one, or close an already open one,
# so we have to keep track of how many are open and how many are left to close at 
# each node of the tree
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []

        def recurse(a: str, o: int, c: int):
            if c >= n:
                answers.append(a)
                return
            
            # open a new one
            if o < n:
                recurse(a + "(", o + 1, c)

            # # close an open one
            if o > c:
                recurse(a + ")", o, c + 1)

        recurse("", 0, 0)
        return answers