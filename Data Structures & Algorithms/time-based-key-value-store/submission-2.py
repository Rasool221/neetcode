class TimeMap:
    def __init__(self):
        self.tmap = {} # key -> timestamp array (increasing order)
        self.vmap = {} # timestamp -> value

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap:
            self.tmap[key].append(timestamp)
        else:
            self.tmap[key] = [timestamp]

        self.vmap[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""
        
        # print(self.tmap, key, timestamp)

        timestamps = self.tmap[key]
        if timestamps[len(timestamps)-1] <= timestamp:
            return self.vmap[timestamps[len(timestamps)-1]]
        
        if timestamps[0] > timestamp:
            return ""

        lower = 0
        upper = len(timestamps) - 1

        last_timestamp_index = 0

        while lower <= upper:
            m = (lower + upper) // 2
            mn = timestamps[m]
            
            if mn <= timestamp:
                last_timestamp_index = m

            if mn > timestamp:
                upper = m - 1
            elif mn < timestamp:
                lower = m + 1
            else:
                return self.vmap[mn]
                
        # print(self.vmap, last_timestamp_index)
        return self.vmap[timestamps[last_timestamp_index]]

