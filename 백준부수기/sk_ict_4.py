import collections


def solution(n, edges):
    nodes = [[] for _ in range(n)]
    for n1, n2 in edges:
        nodes[n1].append(n2)
        nodes[n2].append(n1)
    answer = 0
    
    for i in range(n):
        deq = collections.deque()
        deq.append(([i],[i],i))

        while deq:
            triple, visited, point = deq.popleft()

            if len(triple) == 3:
                answer += 1
                continue

            for j in nodes[point]:
                if j in visited:
                    continue
                deq.append((triple+[j], visited+[j], j))
                deq.append((triple, visited+[j], j))

    return answer


print(solution(4,[[2,3],[0,1],[1,2]]))