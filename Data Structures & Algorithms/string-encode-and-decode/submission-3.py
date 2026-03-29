class Solution:
    def encode_str(self, s: str):
        if len(s) == 0:
            return "empty".encode("utf-8").hex()
        return s.encode("utf-8").hex()
    
    def decode_str(self, s: str):
        decoded = bytes.fromhex(s).decode("utf-8")
        if decoded == "empty":
            return ""
        return decoded

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return ",".join(self.encode_str(s) for s in strs)

            

    def decode(self, s: str) -> List[str]:
        hex_arr = s.split(",")
        if s == "":
            return []
        return [self.decode_str(s) for s in hex_arr]
