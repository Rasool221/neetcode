# i think we can solve this rather easily with 
# dfs over the entire board 
# but lets do a backtracking solution (worse time complexity lol)
# to practice

# i think we build a decision tree search nearby cells and attempt
# to build the word. if we've exceeded the current path, we will return
# from that path and try another one in a different direction
# if the word we built so far is the given word, we've found it and can break out early
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False

        def recurse(i: int, j: int, si: int, mem: set):
            nonlocal exists

            c = board[i][j]
            pos = (i, j)

            if pos in mem:
                return

            # prune tree early
            if si > len(word) - 1 or c != word[si]:
                return

            # if we've found, collapse call stack and return
            if exists or (si == len(word) - 1 and c == word[si]):
                exists = True
                return

            # at each decision tree node
            # we either found a letter and pass it down the tree
            # or we haven't yet, and keep searching in every direction
            right = j < len(board[i]) - 1
            left = j > 0 
            up = i > 0
            down = i < len(board) - 1 

            # add to mem of this branch
            mem.add(pos)

            if right:
                recurse(i, j + 1, si + 1, mem) 

            if left:
                recurse(i, j - 1, si + 1, mem)

            if up:
                recurse(i - 1, j, si + 1, mem)
            
            if down:
                recurse(i + 1, j, si + 1, mem)

            # remove from mem of this branch, nothing worked
            mem.remove(pos)

        for i in range(len(board)):
            for j in range(len(board[i])):
                recurse(i, j, 0, set())
    
        return exists
        