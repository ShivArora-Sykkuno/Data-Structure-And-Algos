class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxx , left, right, basket = 0, 0, 0, {}
        
        while right < len(fruits):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left +=1
            
            if len(basket) <= 2:
                maxx = max(maxx, right - left + 1)
            right +=1
        
        return maxx
    
    