class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decoder = {" ": " "}
        
        cnt = 0
        for idx in key:
            if idx not in decoder:
                decoder[idx] = alphabet[cnt]
                cnt += 1
        
        decode = []
        for idx in message:
            decode.append(decoder[idx])
        
        return "".join(decode)