def solution(s):
    count = 0

    front = 0
    rear = n-1

    while front < rear:
        if s[front] == 'a':
            front += 1
        elif s[rear] == 'b':
            rear -= 1
        else:
            count += 1
            front += 1
            rear -= 1
    
    return count


s = input()
n = len(s)

answer = float('inf')
for i in range(n):
    answer = min(answer, solution(s))
    s = s[n-1] + s[:n-1]

print(answer)