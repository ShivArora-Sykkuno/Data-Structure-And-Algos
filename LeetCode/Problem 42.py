class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        left_max, right_max = height[0] , height[-1]
        summ = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max,height[l])
                summ += left_max - height[l]            
            else:
                r-=1
                right_max=max(right_max,height[r])
                summ += right_max - height[r]
        return summ
        


