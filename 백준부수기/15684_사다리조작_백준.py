import collections
import heapq


def get_start(n, m, visited):
    for row in range(m):
        for col in range(n-1):
            if visited(row, col) == False:
                return (row, col)
    else:
        return -1
        

def play_ladder(init_lines, ss):
    deq = collections.deque()
    deq.append((init_lines, ss))

    while deq:
        lines, ss = deq.popleft()
        success = ladder_check(lines)

        if success:
            break
        
        for row in range(ss[0], m):
            for col in range(n-1):
                if row == ss[0] and col <ss[1]:
                    continue
                deq.append(init_lines + [(row, col)], )

        print(lines)



def ladder_check(lines):
    result = [i for i in range(n)]
    print(lines)
    for k in range(len(lines)):
        print(result)
        row, col = heapq.heappop(lines)
        result[col], result[col+1] = result[col+1], result[col]
    print(result)

    for col in range(len(result)):
        if result[col] != col:
            return False
    else:
        return True


n, m, h = map(int,input().split())
ladder_list = []

for _ in range(m):
    row, col = map(lambda x: int(x)-1 ,input().split())
    ladder_list.append((row, col))

ladder_list.sort()

visited = [[False]*n for _ in range(m)]

for row, col in ladder_list:
    if 0 < col < m:
        visited[row][col-1] = True
    visited[row][col] = True
    visited[row][col+1] = True

start = get_start(n, m, visited)

print(start)
if start == -1:
    result = ladder_check(ladder_list)

else:
    result = play_ladder(ladder_list, start)

print(result)