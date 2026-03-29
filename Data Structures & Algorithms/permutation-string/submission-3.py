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
class Solution:
    def compareMaps(self, s1: dict, s2: dict) -> bool:
        print(s1, s2)
        for k,v in s1.items():
            if k not in s2:
                return False
            
            ks2 = s2[k]
            if v != ks2:
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
        for i in range(len(s2)):
            c = s2[i]
            
            if c in s1_chars:            
                rci = i
                rc = s2[rci]
                while rc in s1_chars and rci <= len(s2) - 1: 
                    if rc not in s2_chars:
                        s2_chars[rc] = 1
                    else:
                        if s2_chars[rc] == s1_chars[rc]:
                            break
                        s2_chars[rc] = s2_chars[rc] + 1

                    rci += 1
                    if rci <= len(s2) - 1:
                        rc = s2[rci]
                
                if self.compareMaps(s1_chars, s2_chars):
                    return True
                
                s2_chars = {}

        return False