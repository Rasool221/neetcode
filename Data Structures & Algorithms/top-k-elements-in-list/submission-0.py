class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                m[n] = m[n]+1
        ans=[]
        for n,l in m.items():
            if l >= k:
                ans.append(n)

        return ans