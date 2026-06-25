# my first instinct was to use a stack but i think that's exactly what '*' discourages
# in this problem. e.g. if we have ((**) as the input and we push '*' onto the stack
# we would need some logic when visiting the last ')' to change '*' as empty string
# maybe a stack does work and we just treat '*' as the greedy next step to validate a string
# then check back when seeing ')' to change how we interpret '*' as an empty string.

# hmm, let's think how we can do this efficiently.
# we can keep a list of used '*' as the greedy next char to validate the string
# then pop off that list. effictively 2 stacks. trying to think of a test case where
# this wouldnt work but its hard to tell. 

# ((**)
# i = 0, st = [(], a = []
# i = 1, st = [((], a = []
# i = 2, st = [(], a = [*] <-- we treated '*' as a ')' and pushed to our second stack
# i = 3, st = [], a = [*, *] <--- same as above
# i = 4, st = [], a = [*] <--- we found a ')' which means we need to take 1 '*' away (treating it as empty string)

# i think this can work, let me give the impl a shot. obv with error checking
# to return false if we cannot find a solution

# this is an O(n) time & space solution which is acceptable for this problem

# ah okay im stupid i only accounted for when strings have '*' so let
# me adjust this to actually do the basic implementation as well if we dont have '*'

# okay that worked for 4 test cases, now we're failing at (*))
# we're returning false when we should be returning true. that is because the
# problem description is stating we can also treat '*' as open paranethesis 

# i wonder if we can fit that into our model here hmm
# we dont even need a stack for our '*', we can just keep a count of how many we've used
# and how many we can use. the ones we dont use at the end are the empty string ones

# then we hit a ')' and stack is empty and have an '*', we 'use' it as an opening paranthesis

# im thinking the reason we keep track of how many we've used is for error tracking and knowing 

# let's run through an example:
# (*))
# i = 0, st = [(], h = 0, u = 0
# i = 1, st = [], h = 0, u = 1 <-- we have assumed '*' is ')'
# i = 2, st = [], h = 1, u = 0 <--- we have consumed ')' as close and restored '*' for later usage
# i = 3, st = [], h = 0, u = 0 <--- when we found ')' and nothing in stack, we used '*' as '('

# i think this should work, let's implement it 

# nice this works for 8/25 test cases but i got this one which fails:
# s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
# yep, im not goiing to debug this by hand. time for a hint

# okay, im way off. well, i think my intuition is right but i need to think in terms of ranges

# if we have a '(' char we widen the range of open paranthesis
# if we have ')' we shorten the range
# if we have '*' we adjust bounds in both directions

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            if max_open < 0:
                return False

            min_open = max(min_open, 0)

        return min_open == 0