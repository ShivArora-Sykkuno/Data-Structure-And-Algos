class Solution:
    def __init__(self):
        self.res = []

    def solve(self, candidates, index, total, target, sub):
        if total == target:
            self.res.append(sub.copy())
            return
        if total > target:
            return
        if index >= len(candidates):
            return
        sub.append(candidates[index])
        summ = total + candidates[index]
        self.solve(candidates, index, summ, target, sub)
        sub.pop()
        summ = total
        self.solve(candidates, index + 1, summ, target, sub)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.solve(candidates, 0, 0, target,[])
        return self.res