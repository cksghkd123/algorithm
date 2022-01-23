In = list(input())
expression = ['']
for i in range(len(In)):
    if In[i] == '+':
        expression[-1] = int(expression[-1])
        expression.append('+')
    elif In[i] == '-':
        expression[-1] = int(expression[-1])
        expression.append('-')
    else:
        if expression == [] or expression[-1] == '+' or expression[-1] == '-':
            expression.append(In[i])
        else:
            expression[-1] = expression[-1] + In[i]

expression[-1] = int(expression[-1])

result = 0
button = False
for i in expression:
    if i == '-':
        button = True
    elif i == '+':
        continue
    else:
        if button == False:
            result += i
        elif button == True:
            result -= i

print(result)
