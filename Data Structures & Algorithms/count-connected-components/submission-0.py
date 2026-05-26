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
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = {}
        component_lookup = {}

        component_count = 0

        for index, edge in enumerate(edges):
            a = edge[0]
            b = edge[1]

            # there are a few cases:
            # 1. a has no component and b has no component:
            #    - index both in component_lookup sharing the same component set ref 
            # 2. a has component and b has no component:
            #    - index b in component_lookup, give it the same set ref as a, and add b to that set
            # 3. b has no component and a has component (i dont know if this case is possible but we will handle it just in case)
            #    - same as option 2 just inverse
            # 4. a has component and b has component:
            #    - the only case here is that if they're in separate components,
            #      in which case we merge them

            # 1
            if a not in component_lookup and b not in component_lookup:
                set_ref = set([a, b])
                component_lookup[a] = set_ref
                component_lookup[b] = set_ref
                component_count += 1
            # 2
            elif a in component_lookup and b not in component_lookup:
                component_lookup[a].add(b)
                component_lookup[b] = component_lookup[a]
            # 3
            elif b in component_lookup and a not in component_lookup:
                component_lookup[b].add(a)
                component_lookup[a] = component_lookup[b]
            # 4
            elif a in component_lookup and b in component_lookup: 
                a_component = component_lookup[a]
                b_component = component_lookup[b]

                # merge both into a
                if a != b:  
                    component_lookup[a] = a_component | b_component
                    component_lookup[b] = component_lookup[a]
                    component_count -= 1

        return component_count
                