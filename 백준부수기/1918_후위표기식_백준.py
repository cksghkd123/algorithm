infix_str = input()
postfix_str = ''
index = 0
def translate():
    global infix_str
    global postfix_str
    global index
    que = []

    while index <len(infix_str):
        c = infix_str[index]
        if c.isalpha():
            postfix_str += c
        else:
            if c == '(':
                index += 1
                translate()
            elif c == ')':
                while que:
                    postfix_str += que.pop()
                return
            elif que:
                if c == '*' or c == '/':
                    if que[-1] == '*' or que[-1] == '/':
                        postfix_str += que.pop()
                    que.append(c)
                else:
                    while que:
                        postfix_str += que.pop()
                    que.append(c)
            else:
                que.append(c)
        index += 1
    
    while que:
        postfix_str += que.pop()

translate()
print(postfix_str)
        
