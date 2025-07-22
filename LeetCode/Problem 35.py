class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ub = len(nums)
        low, high = 0, len(nums)-1
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ub = mid
                high = mid - 1
            elif  nums[mid] < target:
                low = mid +1
            
        return ub
