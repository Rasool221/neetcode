# im having some trouble understanding this problem but i think ive pieced together this so far:
# - we are given edges to a graph with 1 to n nodes.
# - the graph contains 1 extra edge that makes the graph cyclical
# - we should return the edge that makes the graph cyclical, if there are multiple answers, return the last edge in the graph

# hmm, what if the last edge of the graph isnt part of the many edges that make this graph cyclical?
# ah so we're meant to return only the last edge that causes a cycle not the last edge in the list

# my thinking seems a bit naive, but im willing to take the chance and fail just so i can learn
# why it is naive. essentially, im thinking of using BFS, starting from the first element, then going forward.
# i would keep a set of nodes i've seen already during my BFS path, and check if the current path
# is attempting to return to a previous point i've already visited, hence a cycle.

# i would keep track of all of the edges that cause a cycle and return the only element or the last element in that list

# im also assuming that this problem will always give you a test case with a cyclical graph, so if my alg doesnt find a cycle,
# something is clearly wrong
from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        answers = []

        # node -> [] neighbors
        graph = {}

        # creating the graph
        for a, b in edges:
            if a not in graph:
                graph[a] = []

            graph[a].append(b)

        # we dont need to populate graph with nodes that dont appear in edges
        # since we're given a connected (per spec) cyclic graph, all nodes have an edge in edges

        # now we can do BFS, starting from node 1
        # i think we can safely start from node 1 because the problem guaruntees components = 1 (connected per spec)
        
        # queue contains 
        q = deque([(1, set([1]))])

        while q:
            node, visited = q.popleft()

            # for every neighbor, mark it as visited, and then visit it
            # but check if what we're about to enque has been visited
            # if a cycle is detected, we mark it in answers and then skip visiting
            # the node that causes a cycle
            for neighbor in graph[node]:
                if neighbor in visited:
                    answers.append([node, neighbor])
                else:
                    visited.add(neighbor)
                    q.append((neighbor, visited))
        
        return answers

