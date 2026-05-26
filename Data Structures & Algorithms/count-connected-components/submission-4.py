# this is interesting, i obviously need to traverse the graph somehow
# maybe DFS or BFS are both viable here

# however, i almost wonder if simply checking which number in the adjacency list 
# is repeated between each edge. maybe some clever way to do this is a good approach here

# what about the DFS route though, where would you start? and BFS?

# maybe its BFS with multiple starting points

# before i go down that route, i need to try the simple stupid idea i had first
# to see if any test case would fail it, well probably one where we keep a components
# some data structure, as soon as we spot a new component, we would make space for it, then if 
# suddenly we come across an adjacency that bridges two components we didnt have bridged before, we combine them
# into 1 component. 

# but hmm, what data structure helps here

# okay i did this just using hashmaps and set, passed 2 first test cases but not the third, let's take a look at the third
# n=5
# edges=[[0,1],[1,2],[0,2],[3,4]]

# i think what's sketchy is branch #4 down there
# however its valid to subtract from component_count in that case
# what's sketchy is my a != b function, i think we need to do a set overlap check instead of set != set

# i was just using wrong vars, that worked, but we will revisit that overlap idea. now we're failing on test case:
# n=4
# edges=[[2,3],[1,2],[1,3]]
# expected output: 2
# actual output: 1

# wait did i misread this problem? why is that expected output 2?
# ah its because n is given as an input and n = 4 which means there is a lone node 4
# in that case, i will keep a master set of all components, then iterate over n, incrementing
# the component_count as an n appears that is not in the master set
# actually i can just use component_lookup as this master set lol

# woo okay 31/34 test cases pass, we failed on this one
# n=10
# edges=[[5,6],[0,2],[1,7],[5,9],[1,8],[3,4],[0,6],[0,7],[0,3],[8,9]]
# Your Output: 0
# Expected output: 1
# this one is big, im going to draw it out 

# alright i put a duct tape fix around this but im not aware of this is a proper solution anymore
# probably not lol. the next test case im failing im off by 3 and the case is n=500 so there's no way im going to debug
# that manually. im going to look at the hints to see how disgunstingly im off,
# however, i am very happy i got to 33/34 test cases passed with this stupid approach

# alright this is a union find problem, a new concept to me, and it looks like i implmeneted
# a trash and buggy version of it out of a whim. im actually very proud of that, it seems like i understood
# what it took to solve this problem, or atleast the underlying pattern in the datastructure and merging
# but i now need to do it properly!

# alright for union find, we need to support 2 operations:
# - find(n): find which tree n belongs to
# - union(a, b): combine two trees together 
# we would start with components = n, and everytime we call union(a, b), we decrement by 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # every node is a parent of itself initially
        parent = [i for i in range(n)]
        component_count = n

        def find(i: int):
            # walk up the tree until we find the root node
            # for the tree that i lives in
            while parent[i] != i:
                i = parent[i]
                
            return i

        def union(a: int, b: int) -> bool:
            root_a = find(a)
            root_b = find(b)

            # if root of 2 trees dont equal eachother
            # change b's root to a's root
            if root_a != root_b:
                parent[root_b] = root_a
                return True

            return False

        for edge in edges:
            a = edge[0]
            b = edge[1]

            # if we've merged the 2 trees,
            # decrement component_count
            if union(a, b):
                component_count -= 1

        return component_count
                