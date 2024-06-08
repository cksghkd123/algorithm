n = int(input())
m = int(input())
s = input()
answer = 0

i = 0

while i < m - (2*n+1):
    if s[i] == 'I':
        for k in range(2*n+1):
            if k%2 == 0:
                if s[i+k] == 'O':
                    break
            else:
                if s[i+k] == 'I':
                    break
        else:
            answer += 1

    i += 1

print(answer)