# i think we just start from any point (maybe first one?)
# and then in O(n^2) calc min manhatten distance from current point, and connect it to min one
# if more than one tie for min, we connect all of them, then keep global cost and move on

# now we need to keep track of edges from->to and make sure
# we don't re-do work, as well as not adding a connection where a smaller one as been made already

# nope, this is prims alg problem, let's pivot

# prim's alg helps you construct a minimum spanning tree
# for an undirected graph, which is exactly what this problem
# is calling for.

# prim's alg works by:
# - grows a tree one node at a time
# - always adds the single cheapest edge that connects the
#   tree to a node not yet it in
# - maintain min heap and repeatedly pop the minimum
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def mhd(xi: int, yi: int, xj: int, yj: int) -> int:
            return abs(xi - xj) + abs(yi - yj)

        # tuple[cost, index]
        h = [(0, 0)]
        answer = 0
        visited = set()

        # finish when you visit every node once
        while len(visited) < len(points):
            cost, i = heapq.heappop(h)

            # visit every node only once
            if i in visited:
                continue

            # now this node is officially visited
            visited.add(i)
            answer += cost

            # now for every node in the graph,
            # calc cost and add it to heap
            # it will get popped and marked as visited
            # once its the closest next one
            for j in range(len(points)):
                # dont do same work again
                if j in visited:
                    continue

                xi, yi = points[i]
                xj, yj = points[j]
                
                d = mhd(xi, yi, xj, yj)
                entry = (d, j)

                heapq.heappush(h, entry)

        return answer

