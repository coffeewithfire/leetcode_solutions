import typing
import random as rnd

def checkSubarraySum(nums: list[int], k: int) -> bool:
    curSumMod = 0
    hashmap = {}

    for i, n in enumerate(nums):
        curSumMod = (curSumMod + n) % k
        if curSumMod == 0 and i != 0:
            return True
        if curSumMod in hashmap and hashmap[curSumMod] < i - 1:
            return True
        if curSumMod not in hashmap:
            hashmap[curSumMod] = i
    return False

nums = [rnd.randint(0, 100) for _ in range(32)]
print(nums, checkSubarraySum(nums, 13), sep = '\n')
