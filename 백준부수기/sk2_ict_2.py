from collections import deque
import heapq


def solution(arr, processes):
    answer = [None]
    index = 0
    processes = deque(processes)
    process = None
    reading = []
    writing = []
    w_reading = deque()
    w_writing = deque()
    spending_time = 0 

    for i in range(50):
        if processes and process == None:
            process = processes.popleft()
            process = process.split()
        if process != None and str(i) == process[1]:
            if process[0] == "read":
                w_reading.append(list(map(int,process[2:]))+[index])
                answer.append(None)
                index += 1

            elif process[0] == "write":
                w_writing.append(list(map(int,process[2:])))
    
            process = None

        if reading:
            if not w_writing and w_reading:
                while w_reading:
                    t2, a, b, reading_index = w_reading.popleft()
                    heapq.heappush(reading,[i+t2, a, b, reading_index])
            while(reading and i == reading[0][0]):
                _, a, b, reading_index = heapq.heappop(reading)
                answer[reading_index] = "".join(arr[a:b+1])
            spending_time += 1
        
        elif writing:
            if i == writing[0]:
                for j in range(writing[1],writing[2]+1):
                    arr[j] = str(writing[3])
                writing = []
            spending_time += 1

        if not reading and not writing:
            if w_writing:
                t2, a, b, c = w_writing.popleft()
                writing = [i+t2, a, b, c]
            elif w_reading:
                while w_reading:
                    t2, a, b, reading_index = w_reading.popleft()
                    heapq.heappush(reading,[i+t2, a, b, reading_index])
                
        

    answer[index] = str(spending_time)
    return answer


a = solution(["1","1","1","1","1","1","1"],["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"])
print(a)
#["24","3415","4922","12492215","13"]