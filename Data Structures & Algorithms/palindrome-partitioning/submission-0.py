# build a string for every path of the decision tree with the current char 
# i think we take 2 paths:
# - current char only because every 1 char is a palindrome (do not take any mor chars)
# - check if the current char is forming a palindrom (from the passed on string, appending current char to string we're building)
#   (i think we can use a helper method for this and figure out how to speed it up later)
#   if so, keep building
#   if not, prune that branch 

# okay so for the given input "aab"
# this solution produces [["b"],["a"],["a"],["aa"]]
# and we should actually produce [["a","a","b"],["aa","b"]]

# what's happening is that each subarray represents a method of creating a palindrome,
# for example the first one ["a", "a", "b"] is the case where you only take the first letter
# the second one ["aa", "b"] is the case where you take more than one letter AND take one letter
# so i think i need to build that instead, to do that, we dont keep a string and pass it down the tree
# rather we build an array and pass it down the tree with the following decisions:
# - take the next letter as its own string
# - take the next letter if it builds a palandrome with the last string
# our base case will only be if we're surpassed the length of input string, since we wont activate branches we're not sure about anymore (case 2 from above)

# one more revision, i think we loop over all lists in the current branch and see if cur char makes a palindrome with each
# if it does, we create a new branch where we add cur char to that element
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answers = []

        def is_palindrome(string: str) -> bool:
            return len(string) == 1 or string[::-1] == string

        def recurse(i: int, ss: list[str]):
            nonlocal answers

            # add the answer and return if we've surpassed the length of input string
            # bc if we've made it to the end, we have a palindrome, branch didn't prune
            if i >= len(s):
                answers.append(ss)
                return

            c = s[i]
            
            # don't append current char
            recurse(i + 1, ss + [c])

            # iterate through all items with array, create branch with each
            # if cur char forms a palindrome
            ss_copy = ss.copy()
            for mi in range(len(ss)):
                m = ss_copy[mi]
                new_str = m + c
                if is_palindrome(new_str):
                    ss_copy[mi] = new_str
                    recurse(i + 1, ss_copy)

        recurse(0, [])
        return answers