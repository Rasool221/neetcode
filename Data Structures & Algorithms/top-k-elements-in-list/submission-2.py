class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                m[n] = m[n]+1

        nc = list(m.items())
        nc.sort(key=lambda t: t[1], reverse=True)
        return [k for k, _ in nc[0:k]]