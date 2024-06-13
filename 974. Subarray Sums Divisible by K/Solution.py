import typing
from collections import defaultdict

def subarraysDIvByK(nums: list[int], k: int) -> int:
    prefSum = []
    curSum = 0
    for n in nums:
        curSum += n
        prefSum.append(curSum % k)

    seen = defaultdict(int)
    ans = 0
    for n in prefSum:
        if n == 0:
            ans += 1
        if n in seen:
            ans += seen[n]
        seen[n] += 1
    
    return ans

print(subarraysDIvByK([4, 5, 0, -2, -3, 1], 5))