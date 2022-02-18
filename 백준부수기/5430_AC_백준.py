t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    array = input().rstrip(']').lstrip('[').split(',')

    button = 1
    left = 0
    right = 0

    for i in range(len(p)):
        if p[i] == 'R':
            button *= -1
        elif p[i] == 'D':
            if button == 1:
                left += 1
            elif button == -1:
                right += 1

    if left+right > n:
        print('error')
    else:
        answer = '['
        if button == 1:
            for i in array[left:n-right]:
                answer = answer + i + ','
            answer = answer.rstrip(',')
            answer += ']'
        elif button == -1:
            for i in reversed(array[left:n-right]):
                answer = answer + i + ','
            answer = answer.rstrip(',')
            answer += ']'
        print(answer)
    
a = [0,1,2,3,4,5,6,7,8,9]


