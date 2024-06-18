def maxProfitAssigned(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    worker.sort()
    jobs = sorted([{"difficulty" : difficulty, "profit" : profit} for difficulty, profit in zip(difficulty, profit)], 
                  key=lambda x: x["difficulty"])

    lastJobID = 0
    maxProfit = 0
    totalProfit = 0
    
    for ability in worker:
        while lastJobID < len(jobs) and jobs[lastJobID]["difficulty"] <= ability:
            maxProfit = max(maxProfit, jobs[lastJobID]["profit"])
        totalProfit += maxProfit
    
    return totalProfit