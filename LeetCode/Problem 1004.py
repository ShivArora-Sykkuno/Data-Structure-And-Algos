class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

"""
#! only if else condition code sliding window oe frame at a time beats upper code complexity
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxcount = count = 0
        left = right = 0

        while right < len(nums):
            if k > 0:
                if nums[right] == 0:
                    k-=1
                right += 1
                count += 1
            else:
                if nums[right] == 1:
                    right += 1
                    count += 1
                else:
                    if nums[left] == 1:
                        left += 1
                        count -=1
                    else:
                        k+=1
                        left += 1
                        count -= 1

            if count > maxcount:
                maxcount = count
        

        return maxcount
    
"""