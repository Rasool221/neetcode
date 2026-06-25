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
class Solution:
    def checkValidString(self, s: str) -> bool:
        st = [] # our normal stack keeping track of paranthesis
        h, u = 0, 0 # how many '*' we have available for use, and how many we've used

        for i in range(len(s)):
            c = s[i]

            # in case of '(' we simply just add to stack, nothing else
            if c == "(":
                st.append(c)
            elif c == "*":
                # greedily attempt to validate string
                # do nothing if the stack is empty ('*' is empty string)
                if len(st) > 0:
                    st.pop() 
                    u += 1 # keeping track that we've used '*'
            elif c == ")":
                # the following cases to handle:
                # 1. we have no '*' to use and nothing in stack -> invalid string
                # 2. we have '*' and nothing in stack -> use '*' as '('
                # 3. we have no '*' and element in stack -> pop off stack, increment have if used > 0, if not -> invalid string
                # 4. we have '*' and element in stack -> pop off stack
                
                # 1 & 2
                if len(st) == 0:
                    if u == 0:
                        return False

                    # use '*' as '('
                    h -= 1
                    u += 1
                # 3 & 4
                else:
                    # use ')' and restore '*' that we've previously used
                    if h == 0:
                        # only restore '*' if we've used one already
                        if u > 0:
                            u -= 1
                            h += 1
                        
                        # use ')'
                        st.pop()

            # print(f"{i=}, {c=}, {st=}, {h=}, {u=}")

        # if we havent returned False early and 
        # our paranthesis stack is empty, the string is valid
        return len(st) == 0
