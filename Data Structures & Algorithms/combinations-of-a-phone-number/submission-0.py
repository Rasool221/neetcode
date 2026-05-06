# i think we just keep a number to letters mapping as an array and go down the decision tree on what number is next and current
# index + 1, if we hit the amount of digits, we add to an answers array the current string we've built.
# i can imagine mapping the numbers 2-9 dynamically to a-z characters automatically but we will be lazy this time 

# actually, i think its almost like:
#  D   E   F
# GHI GHI GHI
# a for loop that recursively calls a for loop
# passes down a string so far and an index (index of digits, corresponds to a letter )

# at each recursive call, we loop through our digit's letters and add a letter
# we know we're at the end to append if our index has reached the end of digits
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        answers = []

        def recurse(d_i: int, so_far: str):
            nonlocal answers

            if len(so_far) >= len(digits):
                answers.append(so_far)

            if d_i >= len(digits):
                return

            # digit in string format
            d = digits[d_i]
            
            # letters for our digit
            l = m[d]
            for i in range(len(l)):
                c = l[i]
                recurse(d_i + 1, so_far + c)


        recurse(0, "")
        return answers



