class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = 0
        n = len(nums) -1
        jumps = 0
        while right < n:
            far_point = 0
            for i in range(left, right+1):
                far_point =  max(far_point, i + nums[i])

            jumps += 1
            left = right + 1
            right = far_point
        return jumps