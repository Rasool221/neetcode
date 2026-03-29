# position = [1,4], speed = [3,2], target = 10
# pos_speed_arr = [(1, 3, 3), (4, 2, 3)]
# 1 + 3 = 4, 4 + 2 = 6
# 4 + 3 = 7, 6 + 2 = 8
# 7 + 3 = 10, 8 + 2 = 10 <-- fleet
# what does this process look like using a stack?
# steps till target = (target - position) / speed
# how do make this information useful, esp with a stack?
#  

# example 2 pos_speed_arr:
# position = [4, 1, 0, 7]
# speed = [2, 2, 1, 1]
# pos_speed_arr = [(4,2,3), (1,2,4.5), (0, 1, 10), (7,1,3)]
# pos_speed_arr sorted = [(4,2,3), (7,1,3), (1,2,4.5), (0, 1, 10)]
# Keep track of last step, for every step, compare to see if its equal with another  

# example 3
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]
# pos_speed_arr = [(10,2,0) (8,4,1), (0,1,12), (5,1,7), (3,3,2.3)]
# pos_speed_arr sorted = [(10,2,1) (8,4,1), (5,1,7), (3,3,3), (0,1,12)]

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_arr = []
        for i in range(len(position)):
            steps_to_target = (target - position[i]) / speed[i]
            pos_speed_arr.append((position[i], speed[i], steps_to_target))

        pos_speed_arr.sort(key=lambda item: item[0])

        amt_fleet = 0
        last_step = -99999
        while len(pos_speed_arr) > 0:
            item = pos_speed_arr.pop()
            if last_step < item[2]:
                last_step = item[2]
                amt_fleet += 1

        return amt_fleet
            

