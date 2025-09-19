class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def DFS(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                curr.append(candidates[j])
                DFS(j, curr, total+candidates[j])
                curr.pop()
        candidates.sort()
        DFS(0, [], 0)
        return res