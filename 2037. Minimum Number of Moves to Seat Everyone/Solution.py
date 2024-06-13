import typing

def minMowesToSeat(seats: list[int], students: list[int]) -> int:
    # use greedy approach
    seats.sort()
    students.sort()

    ans = 0
    for i, j in zip(seats, students):
        ans += abs(i - j)

    return ans
    
print(minMowesToSeat([3,1,5], [2,7,4]))