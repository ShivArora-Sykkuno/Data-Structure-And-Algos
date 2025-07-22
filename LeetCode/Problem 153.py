class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        mini = float("inf")
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] >= nums[low]:
                if mini > nums[low]:
                    mini = nums[low]
                low = mid + 1
            else:
                if mini > nums[mid]:
                    mini = nums[mid]
                high = mid - 1

        return mini
        