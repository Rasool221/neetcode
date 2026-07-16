import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = {}

        for f, t in tickets:
            if f not in g:
                g[f] = []

            g[f].append(t)
            g[f].sort(reverse=True) # so we can .pop() in O(1)

        answer = []

        def dfs(fr: str):
            if fr in g:
                while g[fr]:
                    dfs(g[fr].pop())

            answer.append(fr)

        dfs("JFK")
        return answer[::-1]



