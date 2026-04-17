import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = [0] * (len(nums) - k) + 1 # how many windows we will have
        max_heap = []
        heapq.heapify_max(max_heap)

        # we keep a max heap that keeps track of current index as well as value

        for i in range(len(nums)):
            n = nums[i]
            is_at_border_of_window = (i + 1) % k == 0

            heapq.heappush_max(max_heap, (n, i))


