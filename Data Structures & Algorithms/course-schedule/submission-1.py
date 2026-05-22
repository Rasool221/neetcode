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

# i think im spot on with the DAG approach, however this test case threw me off:
# numCourses=1
# prerequisites=[]
# expected output: true

# this means there is a course identified as 0 given, and that has no prereqs
# since the prerequisites array is empty. so this means i need to run DFS
# from the starting points WHICH ARE the numbers 0 to numCourses - 1, which clears up
# some confusion i had reading this problem. lets do this

# just realized i also need to update my first pass to build the DAG to 
# build the initial mem hashmap using the numCourses iteration, to handle
# the case of that course not having a prerequisite

# hmm, or maybe that we can just start dfs from course 0, since problem constraints not that it always
# begins with 0 and the return condition is "return true if it is possible to finish all courses, otherwise return false"

# no i dont think that's right since 0 can be its own component and 1 beyond can be in another component
# so we HAVE to dfs from every course

# i think 1 more adjustment we need to make to our mental model is that 
# if course 0 returns false, we should still go to course 1 and attempt a dfs search
# because course 0 isnt a prerequisite, but course 1 is a prerequisite to course 0 

class Node:
    def __init__(self, val: int, neighbors: list['Node']):
        self.val = val
        self.neighbors = neighbors

        self.neighbors_set = set()
        for i in range(len(neighbors)):
            self.neighbors_set.add(neighbors[i].val)

    def __str__(self):
        n = [neighbor.val for neighbor in self.neighbors]
        return f"{self.val=} {n=} {self.neighbors_set=}"

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return False
            
        # keeping track of required, if we find a loop, we can return early
        # int -> Node
        mem = {}
        
        # numCourses represents courses 0 to numCourses - 1
        # so we can build our mem hashmap that we will use later to build
        # the DAG using this, so if we have no prerequisites we can 'just take the class'
        for i in range(numCourses):
            mem[i] = Node(i, [])

        # building the DAG
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

        if len(mem) == 0:
            return False

        # now our DFS function
        # traverse the DAG, return max path found
        def dfs(node: Optional['Node'], depth: int) -> int:
            # base case 1: no node, i dont think its possible but good to have
            if node is None:
                return None

            # print(node)

            # base case 2: no neighbors
            if len(node.neighbors) == 0:
                return depth + 1

            max_depth = 0
            for neighbor in node.neighbors:
                max_depth = max(dfs(neighbor, depth + 1), max_depth)

            return max_depth + 1

        # if one path is valid, then we can take all courses
        valid = False
        for i in range(numCourses):
            node = mem[i]
            max_depth = dfs(node, 0)

            # print(f"{i=} {max_depth=}")
            if max_depth == numCourses:
                return True

        # we can hit all courses if we've reached this part of the code
        # we didnt break out early
        return True

        



            