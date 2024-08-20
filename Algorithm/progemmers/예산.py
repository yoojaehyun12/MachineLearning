def solution(d, budget):
    d.sort()

    for idx, cost in enumerate(d):
        budget -= cost
        if budget < 0:
            return idx

    return len(d)



print(solution([1,3,2,5,4], 9))  # 3
print(solution([2,2,3,3], 10))   # 4







