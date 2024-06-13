import typing

def heightChecker(heights: list[int]) -> int:
    return sum(i - j for i, j in zip(heights, sorted(heights)))

