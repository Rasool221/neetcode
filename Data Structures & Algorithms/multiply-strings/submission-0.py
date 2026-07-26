"""
i think we can just use the unicode 
numbers of the string number characters to go from string -> int

however, i am unsure to go from int -> string. 

wait, i think using ord(n - c) where c is some constant would work, let's see
what that might be:

i=0 ord(str(i))=48
i=1 ord(str(i))=49
i=2 ord(str(i))=50
i=3 ord(str(i))=51
i=4 ord(str(i))=52
i=5 ord(str(i))=53
i=6 ord(str(i))=54
i=7 ord(str(i))=55
i=8 ord(str(i))=56
i=9 ord(str(i))=57

by using chr(n + 48) we can go from int -> str

question is, is this against the rules of this question?
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0

        # unicode ID 48 - 57 are numbers 0-9
        UNICODE_INT_START = 48

        def extend_int(n: int, k: int) -> int:
            return (n * 10) + k

        def str_to_int(char: str) -> int:
            return ord(char) - 48

        def int_to_str(n: int) -> str:
            s = ""

            while n > 0:
                k = n % 10 # get last digit
                s += chr(k + UNICODE_INT_START)
                n //= 10 # remove last digit

            return s[::-1]

        for i in range(max(len(num1), len(num2))):
            if i <= len(num1) - 1:
                k = str_to_int(num1[i])
                num1_int = extend_int(num1_int, k)

            if i <= len(num2) - 1:
                k = str_to_int(num2[i])
                num2_int = extend_int(num2_int, k)

        return int_to_str(num1_int * num2_int)
