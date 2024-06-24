def minKBitFlips(nums: list, k: int) -> int:
    flips = 0
    ans = 0
    for i in range(len(nums)):
        if i >= k and nums[i-k] == 2:
            flips -= 1
        if (nums[i] + flips) % 2 == 0:
            if i + k > len(nums):
                return -1
            nums[i] = 2
            flips += 1
            ans += 1
    return ans