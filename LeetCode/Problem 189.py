class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rot = k % len(nums)
        pos = len(nums) - rot
        nums[:] = nums[pos: ] + nums[: pos]