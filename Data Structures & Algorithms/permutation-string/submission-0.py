# iterate through s2 first
# this problem is very similar to substring, except 
# the order of the substring to find does not matter

# can s1 have repeating chars? i think that will decide the impl

# a brute force solution is o(n^2) where we loop through s2 and find s1
# can we count freq of chars inside s1 and s2? thats technically O(1) space since 
# there are only 26 chars

# after counting chars
# does it have to be contigious?

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        s2_chars = {}

        for c in s1:
            if c not in s1_chars:
                s1_chars[c] = 1
            else:
                s1_chars[c] = s1_chars[c] + 1

        # for c in s2:
        #     if c not in s2_chars:
        #         s2_chars[c] = 1
        #     else:
        #         s2_chars[c] = s2_chars[c] + 1

        # print(s1_chars)

        for c in s2:
            if c in s1_chars:                
                if s1_chars[c] == 0:
                    return False
                s1_chars[c] = s1_chars[c] - 1                    
            # print(c, s1_chars)


        return True