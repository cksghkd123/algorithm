from collections import defaultdict


def solution(goods):
    answer = []
    text_count = defaultdict(int)  

    for g in goods:
        text_length = 1
        overlap_button = defaultdict(lambda: False)
        while text_length <= len(g):
            for i in range(len(g)+1-text_length):
                if overlap_button[g[i:i+text_length]] == False:
                    text_count[g[i:i+text_length]] += 1
                    overlap_button[g[i:i+text_length]] = True
            text_length += 1
    
    for g in goods:
        text_length = 1
        content = set()
        button = False
        while text_length <= len(g):
            for i in range(len(g)+1-text_length):
                if text_count[g[i:i+text_length]] == 1:
                    content.add(g[i:i+text_length])
                    button = True
            if button == True:
                break
            text_length += 1
        
        if content:
            content = sorted(list(content))
            answer.append(' '.join(content))
        else:
            answer.append("None")
    
    return answer


a = solution(["abcdeabcd","cdabe","abce","bcdeab"])
print(a)
#["en nc pe","ico ili lic","a b","u"])
        