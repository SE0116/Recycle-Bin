class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0

        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1]:
                cnt += 1
            else:
                nums[idx-cnt] = nums[idx]

        return len(nums) - cnt