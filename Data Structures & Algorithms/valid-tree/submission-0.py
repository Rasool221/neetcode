class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        seen = set()
        for e in edges:
            to = e[0]
            fr = e[1]

            if fr in seen:
                return False
            else:
                seen.add(fr)

        # for e in edges:
        #     to = e[0]
        #     fr = e[1]

        #     if to in graph:
        #         #graph[to].append(fr)
        #         if fr in graph[to]:
        #             return False
        #         graph[to].add(fr)
        #     else:
        #         #graph[to] = [fr]
        #         graph[to] = set()
        #         graph[to].add(fr)

            # if e[1] in graph:
            #     graph[e[1]].append(e[0])
            # else:
            #     graph[e[1]] = [e[0]]

        # print(graph)

        # seen = set()
        # def dfs(node: int) -> bool:


        return True