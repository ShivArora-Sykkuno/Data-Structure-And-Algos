import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minn_diff = sys.maxsize
        total = 0
        n = len(nums)
        
        print(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                diff = abs(target - summ)
                if diff < minn_diff:
                    minn_diff = diff
                    total = summ
                if summ > target:
                    k -=1
                else:
                    j += 1
        return total