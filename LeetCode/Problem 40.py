class Solution:
    def __init__(self):
        self.res = []

    def solve(self, index, sub, target, candidates):
        if target == 0:
            self.res.append(sub.copy())
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            sub.append(candidates[i])
            self.solve(i + 1, sub, target - candidates[i], candidates)
            sub.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.solve(0, [], target, candidates)
        return self.res
