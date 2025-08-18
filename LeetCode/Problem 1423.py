class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        for i in range(k):
            left_sum += cardPoints[i]
        
        maxx = left_sum
        right_sum, right_index = 0, len(cardPoints)-1
        for j in range(k-1, -1, -1):
            left_sum -= cardPoints[j]
            right_sum += cardPoints[right_index]
            right_index -= 1
            maxx = max(maxx, right_sum + left_sum)
        
        return maxx