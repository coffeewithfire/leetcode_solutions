import random as rnd

def minInrementForUnique(nums: list[int]) -> int:
    nums.sort()
    prev = nums[0]
    moves = 0
    for i in range(1, len(nums)):
        if nums[i] <= prev:
            moves += (prev + 1 - nums[i])
            nums[i] = prev + 1
        prev = nums[i]
    return moves

arr_random = [rnd.randint(0, 20) for _ in range(50)]
arr_test = [3,2,1,2,1,7]

print(minInrementForUnique(arr_random))
print(minInrementForUnique(arr_test))