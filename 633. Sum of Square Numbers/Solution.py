import math

def judgeSquareSum(c: int) -> bool:
    a, b = 0, int(math.sqrt(c))
    while a <= b:
        cur = a * a + b * b
        if cur == c:
            return True
        elif cur < c:
            a += 1
        elif cur > c:
            b -= 1
    return False