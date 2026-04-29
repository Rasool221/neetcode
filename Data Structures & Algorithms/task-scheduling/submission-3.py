# mathematically:
# the number of cycles has to be AT LEAST the amount of identical tasks * n
# because we have to 
# [X, X, Y, Y] with n = 2 would have both X and Y as equally common
# lets call t the amount of non unique chars
# so t = 2, n = 2, t * n = 4, because n = t, we need to add an idle instruction in between for a total instructions of 5

# lets try [a, a, a, b, c], n = 3
# t = 3, n = 3, t * n = 9. t = n here but right answer is 9: [a, b, c, idle, a, idle, idle, idle, a]
# clearly earlier impression wasn't right but i think im on to something, it has to do with other instructions too
# worth looking into just the amount of most recurring instruction
# its almost like its this: t * n

# what if we do [a, a, a, b, c], n = 1
# [a, b, a, c, a] for total of 5. with t = 3, n = 1, this holds up so far

# what about [a, a, a, b, c], n = 2
# [a, b, c, a, idle, idle, a] total = 7
# t = 3, n = 2, t * n = 6
# i think its fair to say that total is at least t * n

# [a, a, a, b, b, c], n = 2
# [a, b, c, a, b, idle, a] total = 7
# t = 3 * n = 6 so i think that tracks with my original note

# obviously we're not getting the answer but at least we have the lower bound of the answer. 
# how do we express that then, in our last example the answer is 7 because we've added 1 idle, because we needed to pad the a at the end
# we can think of t representing [a, <>, <>, a, <> <>, a]. where a is the most common char. we dont realy care about in between values or what they are
# noticing we have a pattern, 2 blocks of [a, <>, <>] and one lone a at the end
# from our previous vars, t and n, each block has size n + 1 because n has to be in between every non-unique char. 
# to achieve [a, <>, <>, a, <>, <>, a] we have (t - 1) * (n - 1) + 1
# the +1 is for the end
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1


        t = max(freq.values())
        c = 0

        for i in freq.keys():
            if freq[i] == t:
                c += 1

        return max((t - 1) * (n + 1) + c, len(tasks))
