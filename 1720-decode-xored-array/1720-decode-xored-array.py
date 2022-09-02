class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for element in encoded:
            arr.append(arr[-1] ^ element)
        return arr
