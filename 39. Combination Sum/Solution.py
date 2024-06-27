def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    cur = []
    def backtrack(i, curSum):
        if curSum > target or i == len(candidates):
            return
        elif curSum == target:
            res.append(cur.copy())
            return
        cur.append(candidates[i])
        backtrack(i, curSum + candidates[i])
        cur.pop()
        backtrack(i + 1, curSum)
    backtrack(0, 0)
    return res