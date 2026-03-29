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

            if fr in graph:
                graph[fr].append(to)
            else:
                graph[fr] = [to]

        print(graph)

        seen = set()
        def dfs(node: int, parent: int) -> bool:
            if node in seen:
                return False
            seen.add(node)
            print(f'{node} - {seen}')
            valid = True
            if node in graph:
                for to in graph[node]:
                    if to == parent:
                        continue
                    result = dfs(to, node)
                    valid = valid and result
            print(f"{node} - {valid}")
            return valid

        return dfs(0, 0) and len(graph) == len(seen)

            
