from collections import defaultdict
import heapq
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     histogram = defaultdict(int)
    #     for num in nums:
    #         histogram[num] +=1
    #     key =list([-i for i in histogram.keys()])
    #     heapq.heapify(key)
    #     cur = 0
    #     while key:
    #         i = heapq.heappop(key) 
    #         cur+=histogram[-i]
    #         if cur >=k:
    #             return -i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        task = nums
        while True:
            if len(task) == 1:
                return task[0]
            pivot = random.randint(0, len(task)-1)
            pivot = task[pivot]
            left_arr = []
            same_arr = []
            right_arr = []
            for number in task:
                if number<pivot:
                    left_arr.append(number)
                elif number == pivot:
                    same_arr.append(number)
                else:
                    right_arr.append(number)
            if len(right_arr)>k:
                task = right_arr
            elif len(right_arr)==k:
                return min(right_arr)
            elif same_arr and len(right_arr)+len(same_arr)>=k:
                return same_arr[0]
            else:
                task = left_arr
                k-=(len(right_arr)+len(same_arr))