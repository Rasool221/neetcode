# aside from the utter confusion of "encode" string -> digits, this problem
# is "decoding" a string INTO digits or rather returning how many possible decodings there
# are, AND the string being actually numbers...this problem is interesting
# we are given a string of numbers, and we are to output how many different ways it can be 
# turned into letters.
# context: A -> 1, B -> 2... Z -> 26
# input: s = "12", output: 2, "12" can be decoded as "AB" (1 2) or "L" (12)
# input: s = "01", output: 0, because 01 is not a valid letter
# important thing to note is that for any number >= 2 && <= 26 it can be mapped to a single letter
# OR multiple letters. however, if its >26 it has to be broken down

# i think we iterate from left to right, attempting to look at the next element to make a letter
# as long as the number <= 26 (combined), we can make on letter.
# in that case, we branch off in 2 paths. take 1 letter only, or attempt to take the second letter
# if the current number is 0, we dont attempt to take next

# ok were at 7/27 passing now, failing at this test case
# s="10", expected output: 1, actual output: 2.
# its because of the second 0, where im moving to next char
# after processing 1 optimistically, but the next char isnt a letter, so we cant add "A" as an
# answer if the next number is 0, we can only join them. therefore, I will only add invidiual n
# to the answer iff next n isn't 0
class Solution:
    def numDecodings(self, s: str) -> int:
        answers = []

        # short circuit early
        if len(s) == 0:
            return 0

        if s[0] == "0":
            return 0

        # i is current index of s
        # returns all possible interpretations of s
        def solve(i: int, so_far: list[str]):
            nonlocal answers

            # print(f"{s=} {i=}")

            # base case, we're at the end 
            # as long as the last n isn't 0, we can return
            # just that letter representation, otherwise, just return
            # what we've built so far
            if i == len(s) - 1:
                n = s[i]
                if n != "0":
                    answers.append(so_far + [n])
                else:
                    answers.append(so_far)
                return

            # if we've overshot i, we can simply just return
            if i > len(s) - 1:
                answers.append(so_far)
                return

            # now, we recurse on only taking the current n at index i
            # and then we look ahead 1 char, if its <= 26 together with current one, we 
            n = s[i]
            n_next = s[i + 1]

            # handling the "0" edge case:
            # - not attempting to join with next n
            # - not adding "0" to the current running answer
            # - not adding individual [n] to current answer if next number is 0
            val_to_add = [n] if n != "0" and n_next != "0" else None

            # recurse by eval cur char and next one only
            # if the next number is not 0 because the next number wont be individually countable
            if val_to_add:
                solve(i + 1, so_far + val_to_add)

            # attempt to join with next char
            combined = int(n + n_next)
            if n != "0" and int(n + n_next) <= 26:
                solve(i + 2, so_far + [n] + [n_next])

        solve(0, [])
        # print(f"{answers=}")
        return len(answers)