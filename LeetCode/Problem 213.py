class Solution:
    def solve(self, n, nums):
        if n == 1:
            return nums[0]
        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            pick = nums[i] + dp[i-2]
            not_pick = 0 + dp[i - 1]
            dp[i] = max(pick, not_pick)
        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]
        ans1 = self.solve(n-1, nums[:n-1])
        ans2 = self.solve(n-1, nums[1: n])
        return max(ans1, ans2)