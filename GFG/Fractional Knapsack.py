class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        
        n = len(val)
        items = [[val[i], wt[i]] for i in range(n)]
        items.sort(key=lambda x: x[0]/x[1], reverse=True)
        
        res = 0
        weight = 0
        for i in range(n):
            if (weight + items[i][1]) <= capacity:
                res += items[i][0]
                weight += items[i][1]
            
            else:
                remain = capacity - weight
                per_ratio = items[i][0] / items[i][1]
                res = res + (per_ratio * remain)
                break
        return res