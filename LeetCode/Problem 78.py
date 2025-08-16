class Solution:
    def __init__(self):
        self.res = []
    def setting(self, nums, index, cpy):
        if index >= len(nums):
            self.res.append(cpy.copy())
            return
        cpy.append(nums[index])
        self.setting(nums, index+1, cpy)
        cpy.pop()
        self.setting(nums, index+1, cpy)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.setting(nums, 0, [])
        return self.res
        