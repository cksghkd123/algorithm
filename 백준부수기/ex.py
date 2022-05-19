import heapq


def solution(alp, cop, problems:list):
    problems.sort()
    heap = []
    heapq.heappush(heap,(0, alp, cop))

    while heap:
        cost, now_alp, now_cop = heapq.heappop(heap)
        heapq.heappush(heap,(cost+1, now_alp+1, now_cop))
        heapq.heappush(heap,(cost+1, now_alp, now_cop+1))
        can_solve = 0
        for problem in problems:
            if now_alp >= problem[0] and now_cop >= problem[1]:
                heapq.heappush(heap,(cost+problem[4], now_alp+problem[2], now_cop+problem[3]))
                can_solve += 1
        if can_solve == len(problems):
            return cost
        


solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])#15
solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])#13