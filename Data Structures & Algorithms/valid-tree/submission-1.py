class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for e in edges:
            to = e[0]
            fr = e[1]

            if to in graph:
                graph[to].append(fr)
            else:
                graph[to] = [fr]

        print(graph)

        seen = set()
        def dfs(node: int) -> bool:
            if node in seen:
                return False
            seen.add(node)
            print(f'{node} - {seen}')
            valid = True
            if node in graph:
                for to in graph[node]:
                    result = dfs(to)
                    valid = valid and result
            print(f"{node} - {valid}")
            return valid

        return dfs(0)

            
