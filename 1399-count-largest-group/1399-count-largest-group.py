class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * (4 * 9)
        
        for idx in range(1, n + 1):
            quotient, reminder = divmod(idx, 10)
            dp[idx] = reminder + dp[quotient]
            counts[dp[idx] - 1] += 1

        return counts.count(max(counts))