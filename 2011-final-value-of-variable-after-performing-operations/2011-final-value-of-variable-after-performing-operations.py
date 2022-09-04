class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cnt = 0
        for idx in range(len(operations)):
            if operations[idx] == "--X" or operations[idx] == "X--":
                cnt -= 1
            else:
                cnt += 1
        return cnt