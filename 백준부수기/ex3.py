import collections


def solution(info, query):
    answer = []
    language = collections.defaultdict(set)
    group  = collections.defaultdict(set)
    carrer = collections.defaultdict(set)
    soulfood = collections.defaultdict(set)
    score = []

    for num in range(len(info)):
        s = info[num].split()
        language[s[0]].add(num)
        group[s[1]].add(num)
        carrer[s[2]].add(num)
        soulfood[s[3]].add(num)
        score.append((int(s[4]), num))
    language['-'].update([i for i in range(len(info))])
    group['-'].update([i for i in range(len(info))])
    carrer['-'].update([i for i in range(len(info))])
    soulfood['-'].update([i for i in range(len(info))])
    score.sort()


    for condition in query:
        c = condition.split(' and ')
        c = c[:3] + c[3].split()
        candidate = set()
        for i in range(len(info)-1, -1, -1):
            if score[i][0] >= int(c[4]):
                candidate.add(score[i][1])
            else:
                break
        result = candidate & language[c[0]] & group[c[1]] & carrer[c[2]] & soulfood[c[3]]
        answer.append(len(result))

    return answer