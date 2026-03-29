class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_solves(cur_m: int, cur_n: int) -> int:
            print("---")
            print("m, n", m, n)

            if cur_m == m and cur_n == n:
                return 1

            solutions = 0
            if cur_m < m:
                solutions += get_solves(cur_m + 1, cur_n)

            if cur_n < n:
                solutions += get_solves(cur_m, cur_n + 1)

            return solutions
        
        return get_solves(1, 1)