class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        for idx in range(0, len(nums), 2):
            for idx2 in range(int(nums[idx])):
                result.append(nums[idx+1])

        return result