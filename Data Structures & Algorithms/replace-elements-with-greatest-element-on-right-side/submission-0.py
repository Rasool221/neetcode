class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix_arr = [0] * len(arr) # suffix sum arr
        suffix_arr[-1] = arr[-1]
        
        for i in range(len(arr)-2, -1, -1):
            suffix_arr[i] = max(arr[i], suffix_arr[i+1])

        for i in range(len(arr)-1):
            arr[i] = suffix_arr[i+1]

        arr[len(arr)-1] = -1
        return arr  