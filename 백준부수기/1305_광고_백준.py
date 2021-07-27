def failure_funtion(text):
    j = 0
    pattern = [0]*len(text)

    for i in range(1, len(text)):
        while j != 0 and text[i] != text[j]:
            j = pattern[j-1]
        if text[i] == text[j]:
            j += 1
            pattern[i] = j
    
    return pattern
             


length = int(input())
line = input()
pi = failure_funtion(line)
answer = length - pi[-1]
print(answer)