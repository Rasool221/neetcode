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
# i = 0, s = [(], a = []
# i = 1, s = [((], a = []
# i = 2, s= [(], a = [*] <-- we treated '*' as a ')' and pushed to our second stack
# i = 3, s = [], a = [*, *] <--- same as above
# i = 4, s = [], a = [*] <--- we found a ')' which means we need to take 1 '*' away (treating it as empty string)

# i think this can work, let me give the impl a shot. obv with error checking
# to return false if we cannot find a solution

# this is an O(n) time & space solution which is acceptable for this problem

# ah okay im stupid i only accounted for when strings have '*' so let
# me adjust this to actually do the basic implementation as well if we dont have '*'
class Solution:
    def checkValidString(self, s: str) -> bool:
        st = [] # our normal stack keeping track of paranthesis
        a = [] # our '*' stack keeping track of wildcards

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                st.append(c)
            elif c == "*":
                # greedily attempt to validate string
                # do nothing if the stack is empty ('*' is empty string)
                if len(st) > 0:
                    st.pop() 
                    a.append("*")
            elif c == ")":
                # if we've used '*', we can pop last one off (treat as empty string)
                # otherwise pop off paranthesis stack, if no elements in there, string is invalid
                if len(a) > 0:
                    a.pop()
                else:
                    if len(st) == 0:
                        return False
                    st.pop()
                    
        # if we havent returned False early and 
        # our paranthesis stack is empty, the string is valid
        return len(st) == 0
