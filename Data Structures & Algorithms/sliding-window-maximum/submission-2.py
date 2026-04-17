import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        max_heap = []
        heapq.heapify_max(max_heap)

        # we keep a max heap that keeps track of current index as well as value
        # every time we're at the border of a window
        #   - we add the current max on the heap to an answer entry
        #     as long as its not outside of the window (lazy approach to dealing with out of window elements)
    
        for i in range(len(nums)):
            n = nums[i]
            is_at_border_of_window = i + 1 >= k # we're at a border of a window at every point after >= k
            heapq.heappush_max(max_heap, (n, i))

            print(f"{n=}, {is_at_border_of_window=}, {max_heap=}")

            if is_at_border_of_window:
                current_max = max_heap[0]
                
                # its possible values outside window are not discarded
                while current_max[1] <= i - k:
                    heapq.heappop_max(max_heap) # discard item from heap, heap will reconstruct
                    current_max = max_heap[0] # set new current_max, inside current window

                current_max_n = current_max[0]
                answer.append(current_max_n)

        return answer


