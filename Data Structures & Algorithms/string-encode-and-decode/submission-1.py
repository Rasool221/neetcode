class Solution:

    def encode(self, strs: List[str]) -> str:
        return ",".join(s.encode("utf-8").hex() for s in strs)

            

    def decode(self, s: str) -> List[str]:
        hex_arr = s.split(",")
        return [bytes.fromhex(s).decode("utf-8") for s in hex_arr]
