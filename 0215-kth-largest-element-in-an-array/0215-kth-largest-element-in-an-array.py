from collections import defaultdict
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        histogram = defaultdict(int)
        for num in nums:
            histogram[num] +=1
        key =list([-i for i in histogram.keys()])
        heapq.heapify(key)
        cur = 0
        while key:
            i = heapq.heappop(key) 
            cur+=histogram[-i]
            if cur >=k:
                return -i
