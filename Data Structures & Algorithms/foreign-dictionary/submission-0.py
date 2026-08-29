"""
look, lets be real. this problem is impractical. 
im looking at hints.

welp, glad i did. pairwise comparison -> graph -> topological sort
"""
from queue import Queue
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set() # stores all unique letters found in words
        g: dict[str, list[str]] = {} # graph of letter -> letters that must go after it
        
        # since words are sorted, lets build a graph u -> v where u
        # is lexographically smalelr than v
        # we can do this by following the facts presented from the problem:
        # - the first letter where words a and b differ is smaller in a than b
        # - a is a prefix of b and a.length < b.length (theres an edgecase to account for with this rule)
        for i in range(len(words) - 1):
            a = words[i] # current word
            b = words[i + 1] # next word, supposed to be lexographically smaller
            
            # just making sure we collect all unique
            # letters in both words
            for c in a:
                letters.add(c)
            for c in b:
                letters.add(c)

            # edge case, if the 2nd condition mentioned in description is violated
            # we will immediately return empty string
            if len(a) > len(b) and a.startswith(b):
                return ""

            # the char index, stop comparing once
            # one of the a[c_i] != b[c_i]
            c_i = 0
            while True:
                # index exceeded one of them or both
                if c_i > len(a) - 1 or c_i > len(b) - 1:
                    break

                ac = a[c_i]
                bc = b[c_i]

                # now, we can make ac -> bc in our graph
                if ac not in g:
                    g[ac] = []


                if ac != bc:
                    g[ac].append(bc)

                # breakout if we need to
                if a[c_i] != b[c_i]:
                    break

                # attempt to keep going
                c_i += 1

        # now we can add other letters to the graph that have no adjacency.
        # this is crucial for the sort later
        for c in letters:
            if c not in g:
                g[c] = []

        # and now, kahn's algorithm
        in_degrees: dict[str, int] = {}

        # building the in_degrees map
        # from the graph we made earlier
        for c, adj in g.items():
            # initial add
            if c not in in_degrees:
                in_degrees[c] = 0

            # now we can add 1 to in_degree count for
            # every adjacency in this list (c -> a)
            for a in adj:
                if a not in in_degrees:
                    in_degrees[a] = 0

                in_degrees[a] += 1

        # print(g)
        # print(in_degrees)

        q = Queue()

        # init the queue with in_degrees equaling 0
        for c, i in in_degrees.items():
            if i == 0:
                q.put(c)

        answer = ""

        # now for the sort:
        # - pop, add to answer
        # - subtract adjacent neighbors in_degree by 1, if they're 0, add to queue
        while not q.empty():
            c = q.get()
            
            # this is a viable answer
            answer += c

            for a in g[c]:
                in_degrees[a] -= 1
                if in_degrees[a] == 0:
                    q.put(a)

        return answer
