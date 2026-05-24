# alright, i think this is the same deal, we have a DAG. in course schedule 1, we 
# just needed to ensure the DAG doesn't have a loop by running DFS. in this one, i think
# we need to run DFS to get to the last course to find if we can make it to the end (valid course schedule)
# and keep track of those paths to return (backtracking)
# if multiple exist we simply return all paths we've found

# im going to copy over the solution from course schedule 1 and modify it

# alright, i think we always need to start DFS from course 0
# and use DFS + backtracking to keep track of answers
# some courses will not have a pre-req, and in that case, we will just
# add it on our DFS run to the current course path we've taken 

# ah i read the question too fast, i am not supposed to return all valid paths
# just any of them. so in that case, once one DFS path reaches the end, i will 
# add it to the global answers array and have a base case in my dfs search that 
# just eliminates rest of branches if that list has any path it in

# now i think all we're missing is a clean way to handle if the course isnt
# in the DAG, which means the course isnt tied to a prereq or isnt a prereq itself,
# in that case we just add it to the path and keep going

# but how do we keep going? these courses can be in the beginning, middle, or end
# anywhere in the sequence hmm
# i think we can just modify our dfs function but "keep going" is a bit strange.
# i think we just keep a counter in our DFS function, that is the current course,
# if its in the DAG, we explore neighbors, if it isnt in the DAG, we move to the next course 

# ah one more adjustment, the classic backtracking thing
# we explore 2 paths at any step, visit a neighbor, and visit the next course
class Node:
    def __init__(self, val: int, neighbors: list['Node']):
        self.val = val
        self.neighbors = neighbors

        self.neighbors_set = set()
        for i in range(len(neighbors)):
            self.neighbors_set.add(neighbors[i].val)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return False

        answer = []
        
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

        has_cycle = False

        # now our DFS function
        # traverse the DAG, mark a global var of max depth
        # if we've detected a cycle, mark a global var
        visited = set()
        def dfs(course: int, path: list[int], cache: set()):
            nonlocal answer
            nonlocal visited

            # node is in the DAG if it is a prereq or another course is a prereq to it
            if course not in mem:
                node = Node(course, [])
            else:
                node = mem[course]

            # base case, return if we've exceeded the numCourses
            if course > numCourses:
                return

            # print(f"{node.val=} {path=}, {cache=}")

            # base case: we've reached the last course, mark
            # the current path as an answer
            # we also need to ensure the answers array would have the full path
            if node.val == numCourses - 1 and len(path) + 1 == numCourses:
                answer = path + [node.val]
                return

            # base case: prune branch if we've already set an answer
            if len(answer) > 0:
                return

            # base case: global visited
            # if this current node has already been visited globally
            # we've arleady proven its cycle free, so let's skip processing this
            if node.val in visited:
                return

            # base case 3: cycle detected in this branch
            if node.val in cache:
                has_cycle = True
                return
            cache.add(node.val)

            # if the current course has neighbors, we recurse on the neighbors (this course is a prereq)
            # if it doesnt, we will just move to the next course
            # recurse on all neighbors
            for neighbor in node.neighbors:
                dfs(neighbor.val, path + [node.val], cache)
            dfs(course + 1, path + [course], cache)

            # remove the current node from cache as to not poison the cache
            # for a branch we're backtracking to
            cache.remove(node.val)

            # global visited addition to not re-do work
            visited.add(node.val)

        # starting from course 0, find all possible paths to
        # the last course
        dfs(0, [], set())
        
        # checking global vars
        return answer
