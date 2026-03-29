import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = {}
        for x, y in points:
            d_from_origin = math.sqrt((x**2) + (y**2))
            m[d_from_origin] = [x,y]

        distance_arr = list(m.items())
        distance_arr.sort(key=lambda i: i[0])

        return [points[1] for points in distance_arr[:k]]