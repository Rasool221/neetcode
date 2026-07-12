# i think since the problem statement is presenting
# a directed and weighted graph, and also
# asking us for the min time to reach all n nodes (reach any node would give same signal)
# then i believe we can try to implement BFS search 
# while counting time, and return the time it took 
# when we visited all nodes

# let's just implement it with a queue and see what happens

# well that requires scanning through all nodes
# but problem statement wants a O(E*log(V)) time
# solution, so this naive approach wont work for 
# what the problem calls for 

# ok naive solution in mind, can we make any optimizations?
# a node has potential to go in many directions, and
# we're trying to find the min amount of time to visit
# all nodes, instead of take all possible paths. 

# this is a bit embarrasing but im keeping in the prev.
# notes. maybe its from being sick for a while or something else
# but i thought BFS would be applicable here, jfc. BFS is not
# implemented to a directed graph. I need to use Dijkstra's here

# this problem can be solved with Dijkstra's
# so let's implement that

# - Dijkstra's over this graph from k (starting point)
# - keep track of total distances to all elements
# - only revisit same element if you can improve its total distance
# - if we didn't visit all elements at end, we can return -1 (>1 graph components)

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # the graph
        # from -> (time, to node index)
        # the reason time is first is because that tuple
        # will be on a min heap which takes first (then second) element
        # as priority, and we need to key prio by time to that node
        g: dict[int, list[tuple[int, int]]] = {} 

        # this list contains our recorded shortest
        # distance to every node
        dist: list[int] = [-1] * n
        dist[k - 1] = 0 # starting point has no delay

        # building graph, including any nodes
        # that may not have edges in times list
        for i in range(n):
            # graph nodes are one indexed
            g[i + 1] = []

        # enriching the graph with edges
        # strictly ui -> vi
        for ui, vi, ti in times:
            # time is first because 
            # first element in tuple in min heap
            # is the priority
            g[ui].append((ti, vi))

        # building our min heap
        # starting from k
        h = heapq.heapify(g[k])
        
        # before entering our loop, we will also
        # populate distances list with distances of 
        # k's neighbors
        for d, i in g[k]:
            # node id's are 1 indexed
            dist[i - 1] = d

        while h:
            # getting top element of heap
            top: tuple[int, int] = heapq.heapppop(h)

            t_dist = top[0] # distance to current node
            t_node_id = top[1] - 1 # id of current node

            # if we've already set a distance
            # for this node, we can skip it as 
            # the first time we find it is the shortest
            # path to it
            if dist[t_node_id] != -1:
                continue

            # get all neighbors, and add to heap if we
            # don't have a distance for them
            for d, i in g[t_node_id]:
                dist[i - 1] = t_dist + d
                heapq.heappush(h, (d, i))
        
        print(dist)

        # if dist contains any -1 values, that means
        # we didnt reach one or more nodes, so we return -1
        # otherwise, we return largest among dist which is shortest
        # time to reach all nodes
        max_d: int = -1
        for d in dist:
            if d == -1:
                return -1
            max_d = max(d, max_d)

        return max_d

            

