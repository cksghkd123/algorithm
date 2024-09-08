S = input()
T = input()

A_count = 0
B_count = 0

S_reverse = ""
for i in range(len(S)-1, -1, -1):
    S_reverse += S[i]

for t in T:
    if t == "A":
        A_count += 1
    elif t == "B":
        B_count += 1

for s in S:
    if s == "A":
        A_count -= 1
    elif s == "B":
        B_count -= 1

def solve(curr, is_reversed, a, b):
    result = 0

    if is_reversed:
        if curr == S_reverse:
            return 1
    else:
        if curr == S:
            return 1
        
    if a > 0:
        if is_reversed:
            if curr[0] == "A":
                result = result | solve(curr[1:], is_reversed, a-1, b)
        else:
            if curr[-1] == "A":
                result = result | solve(curr[:-1], is_reversed, a-1, b)
    
    if b > 0:
        if is_reversed:
            if curr[-1] == "B":
                result = result | solve(curr[:-1], not is_reversed, a, b-1)
        else:
            if curr[0] == "B":
                result = result | solve(curr[1:], not is_reversed, a, b-1)
    
    return result

answer = 0

if A_count >= 0 and B_count >= 0:
   answer = solve(T, False, A_count, B_count)

print(answer)


