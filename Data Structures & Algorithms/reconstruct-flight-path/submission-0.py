import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def p(fr: str, to: str) -> str:
            return f"{fr}->{to}"

        g = {}

        for f, t in tickets:
            if f not in g:
                g[f] = []

            g[f].append(t)
            g[f].sort()

        # JFK is always the starting point
        # first index is current city
        # second index is the path so far
        # third index is a set of from->to strings
        h = [("JFK", ["JFK"], set())]
        heapq.heapify(h)

        while h:
            cur, path, so_far = heapq.heappop(h)
            
            # we've found our path
            # maybe taking the first path isn't right
            if len(path) == len(tickets) + 1:
                return path

            for n in g[cur]:
                id_ = p(cur, n)
                if id_ in so_far:
                    continue

                # since we sorted building the graph
                # the first complete path should be 
                # the answer
                heapq.heappush(
                    h,
                    (n, path + [n], so_far | {id_}),
                )

        # shouldnt happen i guess
        return []


        