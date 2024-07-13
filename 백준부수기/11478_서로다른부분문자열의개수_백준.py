S = input()

final_result = set()

for i in range(len(S)):
    result = ''
    for j in range(i, len(S)):
        result += S[j]
        final_result.add(result)

print(len(final_result))