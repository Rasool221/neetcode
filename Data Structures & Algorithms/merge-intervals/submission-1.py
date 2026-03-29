class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_arr = sorted(intervals, key=lambda interval: interval[0])

        ans_arr = [sorted_arr[0]]
        for i in range(len(sorted_arr)):
            if i == 0:
                continue

            interval = sorted_arr[i]
            start = interval[0]
            end = interval[1]

            last_appended_interval = ans_arr[-1]
            last_start = last_appended_interval[0]
            last_end = last_appended_interval[1]

            if start >= last_start and start <= last_end:
                last_appended_interval[1] = max(end, last_end)
            else:
                ans_arr.append([start, end])

        return ans_arr


            
                
                    
