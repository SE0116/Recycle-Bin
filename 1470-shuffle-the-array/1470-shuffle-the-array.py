class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        
        for idx in range(n):
            result += [nums[idx], nums[idx+n]]
            
        return result