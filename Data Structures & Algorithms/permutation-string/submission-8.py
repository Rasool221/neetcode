# iterate through s2 first
# this problem is very similar to substring, except 
# the order of the substring to find does not matter

# can s1 have repeating chars? i think that will decide the impl

# a brute force solution is o(n^2) where we loop through s2 and find s1
# can we count freq of chars inside s1 and s2? thats technically O(1) space since 
# there are only 26 chars
# 
# does it have to be contigious? -- yes
# how do we keep track of contigiuous?
# combine sliding window with count of chars?
# left and right ptr start at 0 on s2,
# iterate through s2
#   if we find a char that exists in s1_chars
#       start right ptr forward, create temp s2_chars
#           if counts match at end 
#                return True # if we return False on the opposite case here, we risk not finding a substring later
#   return False at end

# this approach is fine for most cases but in cases where chars in s1 are repeated numerous times in s2
# this approach becomes unstable.
# therefore, we have to modify the logic
# iterate through s2
#   if we find a char that exists in s1_chars
#       begin tracking counts
#       start right ptr forward, create temp s2_chars
#           if counts match at end 
#                return True # if we return False on the opposite case here, we risk not finding a substring later
#   return False at end

# that's not a good approach lol
# it works but its not really o(n), so lets think better
# frequency map but sliding window where the window size is s1

class Solution:
    def compareMaps(self, s1: dict, s2: dict) -> bool:
        for k,v in s1.items():
            if k not in s2:
                return False
            
            ks2 = s2[k]
            if v > ks2:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}

        for c in s1:
            if c not in s1_chars:
                s1_chars[c] = 1
            else:
                s1_chars[c] = s1_chars[c] + 1

        s2_chars = {}
        seen = 0
        for i in range(len(s2)):
            c = s2[i]
            if c not in s2_chars:
                s2_chars[c] = 1
            else:
                s2_chars[c] = s2_chars[c] + 1
            seen += 1 
            # print(seen)
            if seen == len(s1):
                # print(s1_chars, s2_chars)
                if self.compareMaps(s1_chars, s2_chars):
                    return True
                seen -= 1
                leftmost_char = s2[i - len(s1) + 1]
                s2_chars[leftmost_char] = s2_chars[leftmost_char] - 1 # removing leftmost char

        return False