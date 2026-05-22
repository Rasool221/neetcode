# alright so i think this is a DAG problem because
# the preqrequisites array represnets a directed graph.
# for example, in the 2nd sample test case we get 
# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
# Output: false
# which forms a DAG like this:
# 0 <-> 1
# which is not a valid directed graph

# given the first example:
# Input: numCourses = 2, prerequisites = [[0,1]]
# Output: true
# the DAG would look like 0 -> 1 
# which is a valid DAG however that's not the only check the perform,
# next we need to validate if we're able to take all of the courses
# in other words, if we're able to visit all of the nodes on this DAG
# we can just use BFS on the DAG and count how many nodes we visit, 
# and if that number matches the numCourses input param, i think
# that means the schedule is valid

# im going to write a helper class for us to form our dag so we can 
# use BFS in an attempt to traverse it

# question is, where do we start the BFS search? from all pre-reqs?
# DFS would work here as well actually, we can do that too

# so if we're given this kind of input:
# Input: numCourses = 4, prerequisites = [[1, 0], [2, 1], [3, 2]]
# Output: true
# DAG: 0 -> 1 -> 2 -> 3

# i think i will actually use DFS here, because we can find a path in the DAG to get
# me all of the courses, rather than a BFS it may be more suitable for shortest path type problems

class Node:
    def __init__(self, val: int, neighbors: list['Node']):
        self.val = val
        self.neighbors = neighbors

        self.neighbors_set = set()
        for i in range(len(neighbors)):
            self.neighbors_set.add(neighbors[i].val)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # keeping track of required, if we find a loop, we can return early
        # int -> Node
        mem = {}

        # first pass, building the DAG
        for pre in prerequisites:
            a = pre[0]
            b = pre[1]

            # cycle check
            # early return False if we've detected a cycle
            if a in mem and b in mem[a].neighbors_set:
                return False

            # building DAG
            # adding a for later cycle checks
            if a not in mem:
                mem[a] = Node(a, [])

            if b in mem:
                mem[b].neighbors.append(mem[a])
            else:
                mem[b] = Node(b, [mem[a]])

            mem[b].neighbors_set.add(mem[a].val)

        # now our DFS function
        # traverse the DAG, return max path found
        def dfs(node: Optional['Node'], depth: int) -> int:
            # base case 1: no node, i dont think its possible but good to have
            if node is None:
                return None

            # base case 2: no neighbors
            if len(node.neighbors) == 0:
                return depth + 1

            max_depth = 0
            for neighbor in node.neighbors:
                max_depth = max(dfs(neighbor, depth + 1), max_depth)

            return max_depth 

        # now we call this DFS function on every starting point
        # because some points in the DAG can have multiple components
        max_depth = 0
        for node in mem.values():
            max_depth = max(dfs(node, 0), max_depth)

        # print(f"{max_depth=}")

        # we can hit all courses if the max depth from any point is
        # the amount of courses, i think lol
        return max_depth == numCourses

        



            