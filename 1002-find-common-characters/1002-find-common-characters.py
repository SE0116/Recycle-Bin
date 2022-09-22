class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        for idx1 in range(len(words[0])):
            for idx2 in range(1, len(words)):
                if words[0][idx1] in words[idx2]:
                    words[idx2] = words[idx2].replace(words[0][idx1], '', 1)
                else:
                    break
            else:
                result.append(words[0][idx1])
                           
        return result