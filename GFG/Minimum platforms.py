class Solution:   
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        
        platforms = 1
        count = 1
        i = 1
        j = 0
        while i < len(arr) and j < len(dep):
            
            if arr[i] <= dep[j]:
                count += 1
                i +=1
            else:
                count -= 1
                j += 1
                
            platforms = max(platforms, count)
        return platforms