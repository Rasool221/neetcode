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

# phew, this solution works, but we are getting time limit exceeded for one test case "efe" lol
# which is only 3 letters. since we had "aab" passing earlier and that case is 3 letters, i think
# we are not pruning early enough or we're going in circles, hmmm

# its much more likely we're going in circles with "efe" test case, because it is 3 letters after all, but where?
# oh, its a bug with NeetCode, when i run this as a submission, it says TLE, but when i run it as a single test case, 
# it i just have the wrong output so no TLE.

# okay so the problem is that im producing [["e","f","e"],["ee","f"]]
# when the right answer should be [["e","f","e"],["efe"]]

# clearly the if im generating "ee" i am skipping over "f", so i need to be careful about that
# to fix this, i think i need to look more than 1 character ahead? "ef" isnt a palindrome, so that branch
# will never get created in order to produce "efe" with the current logic. or maybe i need to branch 
# regardless if it currently generates a palindrome and only add to the answers whats a palindrome out of the list

# the second one sounds slightly more inefficient since we're not pruning early, but the first one sounds very complicated 
# and we can end up in edge case hell
# let's try the first one

# ok this passes for 6 test cases but failes at the 7th:
# Your Output:
# [["e","f","e"],["ee","f"]]
# Expected output:
# [["e","f","e"],["efe"]]

# i think im overcomplicating this, let me try a smarter approach
# by scanning until the next palindrome, if we found one, we add it to the list and recurse
# this should catch 1 char and many characters, replacing our initial approach
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

            for j in range(i, len(s)):
                a = s[i:j+1]
                if is_palindrome(a):
                    recurse(j + 1, ss + [a])

        recurse(0, [])
        return answers