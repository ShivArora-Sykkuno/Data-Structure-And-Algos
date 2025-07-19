class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        hell = 0
        for i in range(len(nums)):
            if nums[i] == nums[(len(nums)//2) + hell]:
                return nums[i]
            else:
                hell += 1