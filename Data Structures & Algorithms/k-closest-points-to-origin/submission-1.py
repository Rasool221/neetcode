import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = {}
        for x, y in points:
            d_from_origin = math.sqrt((x**2) + (y**2))
            
            if d_from_origin in m:
                m[d_from_origin].append([x,y])
            else:
                m[d_from_origin] = [[x,y]]

        distance_arr = list(m.items())
        distance_arr.sort(key=lambda i: i[0])

        # print(distance_arr)

        ans = []
        for i in range(len(distance_arr) - 1):
            if len(ans) == k:
                break
            p = distance_arr[i][1]
            ans += p
            
        return ans