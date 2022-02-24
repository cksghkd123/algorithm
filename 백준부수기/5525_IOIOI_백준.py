n = int(input())
m = int(input())
s = input()
answer = 0

def find(index):
    for k in range(2*n+1):
        if k%2 == 0:
            if s[index+k] == 'O':
                return 0
        else:
            if s[index+k] == 'I':
                return 0
    
    return 1


if 2*n+1 > m:
    print(0)
else:
    for i in range(m-(2*n+1)):
        answer += find(i)

    print(answer)