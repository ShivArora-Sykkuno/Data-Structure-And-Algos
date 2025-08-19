class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump_index = 0
        for i in range(len(nums)):
            if i > max_jump_index:
                break
            max_jump_index = max(max_jump_index, i+nums[i])

        if max_jump_index < len(nums)-1:
            return False
        else:
            return True