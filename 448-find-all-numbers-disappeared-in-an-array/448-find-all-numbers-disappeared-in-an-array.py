class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [idx for idx in range(1, len(nums) + 1) if idx not in s]