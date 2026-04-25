# build trie out of words,
# then search the board 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found_words = []

        # searches board
        # with cache so we dont go in circles
        def dfs(trie: dict, word_so_far: str, i: int, j: int, cache: set):
            nonlocal found_words

            pos = (i, j)
            cache.add(pos)

            c = board[i][j]

            # base case 1, char not found
            if c not in trie:
                return 

            # if we're at end of word, add the word to found words
            # but we don't return
            if "#" in trie[c]:
                new_word = word_so_far + c
                if new_word not in found_words:
                    found_words.append(new_word)
            
            # now we just search left, right, up, or down
            left = j > 0 and (i, j - 1) not in cache
            right = j <= len(board[i]) - 2 and (i, j + 1) not in cache
            up = i > 0 and (i - 1, j) not in cache
            down = i <= len(board) - 2 and (i + 1, j) not in cache

            # print(f"{left=}, {right=}, {up=}, {down=}, {trie[c]=}, {c=}")

            if left:
                dfs(trie[c], word_so_far + c, i, j - 1, cache)
            
            if right:
                dfs(trie[c], word_so_far + c, i, j + 1, cache)

            if up:
                dfs(trie[c], word_so_far + c, i - 1, j, cache)

            if down:
                dfs(trie[c], word_so_far + c, i + 1, j, cache)

            cache.remove(pos)

        trie = {}
        for word in words:
            prev = trie
            for i in range(len(word)):
                flag = i == len(word) - 1 # sentinel indicator
                c = word[i]

                if c not in prev:
                    prev[c] = {}

                prev = prev[c]

                if flag:
                    prev["#"] = True

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(trie, "", i, j, set())

        return found_words
