"""
bellman-ford alg, where we run the relaxtion steps v times to find
negative cycles and mark them with float('-inf'), but snapshot the dist arr at k steps

that should respect our k constraint
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n # dist arr describing distance from src to vertex i
        dist_snapshot = []

        # important for relaxation steps to work
        dist[src] = 0

        # relaxation steps run V - 1 times
        for i in range(n - 1):
            prev = list(dist)
            # for every edge, calc distance
            for fr, to, c in flights:
                if prev[fr] + c < prev[to]:
                    dist[to] = prev[fr] + c

            # taking a snapshot of dist at step k
            if i == k:
                dist_snapshot = list(dist)

        if len(dist) != len(dist_snapshot):
            dist_snapshot = list(dist)
    
        print(dist_snapshot)
    
        # if any vertices in path are unreachable, dest is unreachable
        if (
            dist_snapshot[dst] in [float('inf'), float('-inf')]
        ):
            return -1

        return dist_snapshot[dst]
