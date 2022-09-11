class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        for idx1 in range(len(prices)):
            for idx2 in range(idx1+1, len(prices)):
                if prices[idx2] <= prices[idx1]:
                    prices[idx1] -= prices[idx2]
                    break

        return prices