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

# ok that doesnt work because we flag cycles when we really shouldnt.
# i think we should iterate through edges, then union by rank over each node, and check if they have the same root
# i had to use hints to solve this but since im new to union find algorithms ill give myself a pass here lol
# here are my previous union find notes
# - find(n): find which tree n belongs to
# - union(a, b): combine two trees together 
# on union, if a and b share the same parent that means there is a cycle, and we must
# add return that information. there can be many cycles, so we keep a list of answers and return the last element
# because the edges are given in order, i think we just use that order, if there is a test case where they're not ordered
# then we can perform a sort
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        answers = []

        # problem states we are given edges of length n, so its safe to 
        # initialize the parent array of all nodes are their own parent of size edges (which has to be n)
        # also we're initializing with i + 1 since in this problem the nodes are 1 indexed
        parent = [i + 1 for i in range(len(edges))] 

        # find function will take in node i (but we're using i - 1 on index access since graph gives us 1 indexed nodes),
        # then find its parent node and using path compression
        # on the way back up the call stack
        def find(i):
            p = parent[i - 1] # get the parent
            if i != p: # if we're not at the parent, keep going up
                p = find(parent[i - 1]) # set the parent to the parent of the parent, this is path compression

            # return the eventual parent
            return p

        # take two paths, then find their parent,
        # if it matches, return whether they share the same parent
        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)

            # if the parents dont equal eachother,
            # set b's parent to a's parent and move on
            # this is key to find cycles down the road
            if parent_a != parent_b:
                parent[b - 1] = parent[a - 1]
                return False

            return True

        # iterate through the edges in the order they were given
        for a, b in edges:
            # if this returns True, there is a cycle and we must log it
            if union(a, b):
                answers.append([a,b])

        # given problem description we must have a cycle so its safe to access
        # last element here which works for 1 element or many elements, both cases 
        # is what the problem wants, the first cycle edge or the last one
        return answers[-1]
