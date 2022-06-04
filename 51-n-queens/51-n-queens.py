class Solution:
    def solveNQueens(self, n):
        result = []
        def dfs(queens, diff_, sum_):
            i = len(queens)
            if i == n:
                queens = ['.' * cnt + 'Q' + '.' * (n - 1 - cnt) for cnt in queens]
                result.append(queens)
                return
            for j in range(n):
                if j in queens or i - j in diff_ or i + j in sum_:
                    continue
                dfs(queens + [j],
                    diff_ + [i - j],
                    sum_ + [i + j])
        dfs([], [], [])
        return result