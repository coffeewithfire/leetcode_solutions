def minDays(bloomDay: list[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1
    
    def canMakeBouquetsAtDay(day: int) -> bool:
        bouquets = 0
        flowers_in_row = 0

        for bloom in bloomDay:
            if bloom <= day:
                flowers_in_row += 1
                if flowers_in_row == k:
                    bouquets += 1
                    flowers_in_row = 0
            else:
                flowers_in_row = 0

        return bouquets >= m

    left, right = min(bloomDay), max(bloomDay)
    while left < right:
        mid = (left + right) // 2
        if canMakeBouquetsAtDay(mid):
            right = mid
        else:
            left = mid + 1
    
    return left