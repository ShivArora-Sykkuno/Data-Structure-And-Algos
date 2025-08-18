class Solution:
    def findContentChildren(self, greeds: List[int], cookies: List[int]) -> int:
        greeds.sort()
        cookies.sort()
        res = 0
        ig = cg = 0
        while ig < len(greeds) and cg < len(cookies):
            if greeds[ig] <= cookies[cg]:
                ig += 1
                res +=1
            cg  += 1

        return res
            

        