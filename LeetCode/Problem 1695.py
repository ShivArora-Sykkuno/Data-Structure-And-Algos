class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        curSum = maxSum = 0
        windowVals = set()
        for rightVal in nums:
            while rightVal in windowVals:
                leftVal = nums[left]
                windowVals.remove(leftVal)
                curSum -= leftVal
                left += 1
                
            windowVals.add(rightVal)
            curSum += rightVal
            maxSum = max(curSum, maxSum)
    
        return maxSum