def n_cases(array, result):
    if sum(array) == 0:
        cases.append(result)
        return
    
    for i in range(4):
        if array[i] > 0:
            k = [0, 0, 0, 0]
            k[i] -= 1
            n_cases(list(map(lambda x,y: x+y,array, k)), result + [i])

    

n = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split()))
#0,1,2,3 >> +,-,*,//

cases = list()
n_cases(operators, [])

max_result = float('-inf')
min_result = float('inf')

for c in cases:
    result = numbers[0]
    for i in range(1,len(numbers)):
        if c[i-1] == 0:
            result += numbers[i]
        elif c[i-1] == 1:
            result -= numbers[i]
        elif c[i-1] == 2:
            result *= numbers[i]
        elif c[i-1] == 3:
            if result < 0 and numbers[i] > 0:
                result *= -1
                result //= numbers[i]
                result *= -1
            else:
                result //= numbers[i]
    
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)