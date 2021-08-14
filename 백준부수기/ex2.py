import collections


answer = 0
members = collections.defaultdict(int)
def find(position_list, result, popd_button, pdfe_button):
    if len(result) == len(position_list):
        answer += 1
        return

    if result == []:
        if members['PO'] > 0:
            members['PO'] -= 1
            find(position_list, result + ['PO'], True, pdfe_button)
            members['PO'] += 1
    
    elif popd_button == True:
        if result[-1] == 'PO':
            if members['PD'] > 0:
                members['PD'] -= 1 
                find(position_list, result + ['PD'], False, pdfe_button)
                members['PD'] += 1
        elif result[-1] == 'PD':
            if members['PO'] > 0:
                members['PO'] -= 1
                find(position_list, result + ['PO'], False, pdfe_button)
                members['PO'] += 1
    
    elif pdfe_button != False:
        for i in position_list:
            if members[i] > 0:
                members[i] -= 1
                if members[i] == 'PO':
                    if position_list[-1] == 'PD':
                        find(position_list, result + ['PO'], popd_button, pdfe_button+1)
                    else:
                        find(position_list, result + ['PO'], True, pdfe_button+1)
                elif members[i] == 'PD':
                    if position_list[-1] == 'PO':
                        find(position_list, result + ['PD'], popd_button, pdfe_button+1)
                    else:
                        find(position_list, result + ['PD'], True, 0)
                elif members[i] == 'FE':
                    find(position_list, result + ['FE'], popd_button, 0)
                elif members[i] == 'BE':
                    find(position_list, result + ['BE'], popd_button, pdfe_button)
                members[i] += 1

    else:
        for i in position_list:
            if members[i] > 0:
                members[i] -= 1
                if members[i] == 'PO':
                    if position_list[-1] == 'PD':
                        find(position_list, result + ['PO'], popd_button, pdfe_button)
                    else:
                        find(position_list, result + ['PO'], True, pdfe_button)
                elif members[i] == 'PD':
                    if position_list[-1] == 'PO':
                        find(position_list, result + ['PD'], popd_button, 1)
                    else:
                        find(position_list, result + ['PD'], True, 1)
                elif members[i] == 'FE':
                    find(position_list, result + ['FE'], popd_button, 1)
                elif members[i] == 'BE':
                    find(position_list, result + ['BE'], popd_button, pdfe_button)
                members[i] += 1


def solution(position_list):
    for i in position_list:
        members[i] += 1
    find(position_list, [], False, False)

    return answer



a = ["PO", "PD", "FE", "BE"]
print(solution(a))