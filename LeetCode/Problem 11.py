class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx= 0
        i =0
        j = len(height)-1
        while i < j:
            area = (j-i) * min(height[i], height[j])
            maxx = max(maxx, area)
            if height[i]< height[j]:
                i +=1
            else:
                j -=1
        return maxx
