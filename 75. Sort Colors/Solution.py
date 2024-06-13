import typing
import random as rnd

def sortColors(nums: list[int]) -> None:
    # use three pointers
    l, r = 0, len(nums) - 1
    m = 0

    while m <= r:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 2:
            nums[m], nums[r] = nums[r], nums[m]
            r -= 1
        else:
            m += 1
    
    return None

N = 32
colors = [rnd.randint(0, 2) for _ in range(N)]

print(colors)
sortColors(colors)

print(colors)