import heapq


def distace(a, b):
    result = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(0.5)
    return result

def prim(stars):
    graph = [[] for i in range(n)]

    for i in range(len(stars)):
        for j in range(len(stars)):
            if j == i:
                continue
            graph[i].append((distace(stars[i],stars[j]), i, j))

    connected_nodes = [0]
    candidate_edge_list = graph[0]
    heapq.heapify(candidate_edge_list)
    result = 0

    while candidate_edge_list:
        dis, node1, node2 = heapq.heappop(candidate_edge_list)
        if node2 not in connected_nodes:
            connected_nodes.append(node2)
            result += dis

            for edge in graph[node2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge_list, edge)
    
    print("{:.2f}".format(result))

      

n = int(input())
take_list = [list(map(float, input().split())) for _ in range(n)]
prim(take_list)


