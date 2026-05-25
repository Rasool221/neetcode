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

# another adjustment, 0 cannot be a valid starting point
# aka DAG with 1 -> 0, we have to start from the smallest course in the DAG
# this means we need to do the both of following to boostrap the DFS:
# - start from course 0
# - start from min course in the DAG

# well, scratch all of this. its gotten me commendably far but the real approach to solving
# this problem is kahns algorithm, which is a first for me, so happy to learn it

# here's how it goes:
# - calculate the in_degree for every course, how many courses are prereqs to this one
# - put all courses of in_degree = 0 into a FIFO queue (in order), then enter a loop
# - at each loop iteration pop the top of queue 
#   * add course to answer
#   * for any course that depends on it, subtract 1 from in_degree
#   * if their in_degree drops to 0, add those to the queue as well
# - when queue is empty, check answer to ensure all courses are in the answer, if not
#   we had a cycle and we can instead return []
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []

        answer = []
        
        # course: int -> in_degree: int
        in_degrees = {}
        
        # course: int -> neighbors: list[int]
        neighbors = {}

        # helper set to keep track of what we've seen in prerequisites
        # there might be a better way to do this but i cant think of it 
        seen = set()

        for pre in prerequisites:
            a = pre[0]
            b = pre[1]

            # populating neighbors with
            # b -> [a...]
            if b in neighbors:
                neighbors[b].append(a)
            else:
                neighbors[b] = [a]

            # bumping in_degree of a
            in_degrees[a] = in_degrees.get(a, 0) + 1

            # adding 0 in_degree of b which can later be updated 
            # if it is a in a later iteration
            if b not in in_degrees:
                in_degrees[b] = 0
            
            # giving a empty neighbors if it doesnt
            # have any because we rely on neighbors map
            if a not in neighbors:
                neighbors[a] = []

            seen.add(a)
            seen.add(b)
            
        q = deque([])

        # now populating any courses we missed from prerequisites list
        # all with no neighbors and in_degree of 0
        for i in range(numCourses):
            if i not in seen:
                in_degrees[i] = 0
                neighbors[i] = []

            if in_degrees[i] == 0:
                q.appendleft(i)

        while len(q) > 0:
            top = q.popleft()
            # print(f"{top=} {neighbors=}")
            top_neighbors = neighbors[top]

            # adding course to answer, in_degree is 0
            answer.append(top)
            
            # if course has neighbors, subtract their in_degree by 1
            # if they have reached 0, we can add them to the queue
            for n in top_neighbors:
                in_degrees[n] = in_degrees[n] - 1
                if in_degrees[n] == 0:
                    q.appendleft(n)

        # checking to see if answer found a path
        if len(answer) != len(in_degrees):
            return []

        return answer


            