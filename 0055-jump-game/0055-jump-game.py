class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_value = nums[0]
        for i, num in enumerate(nums):
            if i > max_value:
                return False
            max_value = max(max_value, num+i)
        return True