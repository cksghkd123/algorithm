import requests
import collections


x_auth_token = 'f9aa912c2c31a2abc2536b466a6fbf67'

url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'

def start(x_auth_token, p_number):
    uri = url + '/start'

    return requests.post(uri, headers={'X-Auth-Token': x_auth_token}, json={'problem': p_number}).json()

def waiting_line(auth_key):
    uri = url + '/waiting_line'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

def game_result(auth_key):
    uri = url + '/game_result'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

def user_info(auth_key):
    uri = url + '/user_info'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

def match(auth_key, pairs):
    uri = url + '/match'

    return requests.put(uri, headers={'Authorization': auth_key}, json={"pairs": pairs}).json()

def change_grade(auth_key, commands):
    uri = url + '/change_grade'

    return requests.put(uri, headers={'Authorization': auth_key}, json={"commands": commands}).json()

def score(auth_key):
    uri = url + '/score'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

def p1_simulator():
    auth_key = start(x_auth_token, 1)['auth_key']
    #유저의 매칭 횟수가 늘어남에 따라 grade 획득점수를 줄여감
    user_play_count = collections.defaultdict(int)

    for current_time in range(595):
        print(current_time)
        user_info_list = user_info(auth_key)["user_info"]
        waiting_list = [list(i.values()) for i in waiting_line(auth_key)['waiting_line']]
        waiting_list.sort(key=lambda x: [x[1], x[0]])
        waiting_list = collections.deque(waiting_list)

        #등급조정
        #게임 결과를 등급에 반영
        #유저의 게임 횟수에 따라 차등 반영
        change_grade_commands = []
        for result in game_result(auth_key)["game_result"]:
            count = user_play_count[result["win"]]
            #서로의 등급관계에 따른 차등 반영
            #걸린시간 = 40분 - (두 유저 간 고유 실력 차 / 99000 * 35)
            weight = 1 - (100  - (40 -result["taken"]))/100
            
            if 0 < count <= 2:
                grade = user_info_list[result["win"]-1]['grade'] + int(2000*weight)
                if grade > 9999:
                    grade = 9999
                change_grade_commands.append({"id": result["win"], "grade": grade})
            elif 2 < count <= 4:
                grade = user_info_list[result["win"]-1]['grade'] + int(1600*weight)
                if grade > 9999:
                    grade = 9999
                change_grade_commands.append({"id": result["win"], "grade": grade})
            elif 4 < count <= 6:
                grade = user_info_list[result["win"]-1]['grade'] + int(1200*weight)
                if grade > 9999:
                    grade = 9999
                change_grade_commands.append({"id": result["win"], "grade": grade})
            elif 6 < count <= 8:
                grade = user_info_list[result["win"]-1]['grade'] + int(800*weight)
                if grade > 9999:
                    grade = 9999
                change_grade_commands.append({"id": result["win"], "grade": grade})
            elif 8 < count:
                grade = user_info_list[result["win"]-1]['grade'] + int(400*weight)
                if grade > 9999:
                    grade = 9999
                change_grade_commands.append({"id": result["win"], "grade": grade})

            count = user_play_count[result["lose"]]
            if 0 < count <= 2:
                grade = user_info_list[result["lose"]-1]['grade'] - int(2000*weight)
                if grade < 0:
                    grade = 0
                change_grade_commands.append({"id": result["lose"], "grade": grade})
            elif 2 < count <= 4:
                grade = user_info_list[result["lose"]-1]['grade'] - int(1600*weight)
                if grade < 0:
                    grade = 0
                change_grade_commands.append({"id": result["lose"], "grade": grade})
            elif 4 < count <= 6:
                grade = user_info_list[result["lose"]-1]['grade'] - int(1200*weight)
                if grade < 0:
                    grade = 0
                change_grade_commands.append({"id": result["lose"], "grade": grade})
            elif 6 < count <= 8:
                grade = user_info_list[result["lose"]-1]['grade'] - int(800*weight)
                if grade < 0:
                    grade = 0
                change_grade_commands.append({"id": result["lose"], "grade": grade})
            elif 8 < count:
                grade = user_info_list[result["lose"]-1]['grade'] - int(400*weight)
                if grade < 0:
                    grade = 0
                change_grade_commands.append({"id": result["lose"], "grade": grade})
                
        change_grade(auth_key, change_grade_commands)

        #매칭
        match_commands = []
        matched = []
        while waiting_list:
            user_id, user_from = waiting_list.popleft()
            if user_id in matched:
                continue
            waiting_time = current_time - user_from
            # 기다린 시간에 대해 차등적으로 매칭
            if waiting_time < 2:
                for op_user_id, op_user_from in waiting_list:
                    gap = abs(user_info_list[user_id-1]['grade'] - user_info_list[op_user_id-1]['grade'])
                    if gap < 200:
                        match_commands.append([user_id, op_user_id])
                        user_play_count[user_id] += 1
                        user_play_count[op_user_id] += 1
                        matched.append(op_user_id)
                        break
            elif 2 <= waiting_time < 4:
                for op_user_id, op_user_from in waiting_list:
                    gap = abs(user_info_list[user_id-1]['grade'] - user_info_list[op_user_id-1]['grade'])
                    if gap < 400:
                        match_commands.append([user_id, op_user_id])
                        user_play_count[user_id] += 1
                        user_play_count[op_user_id] += 1
                        matched.append(op_user_id)
                        break
            elif 4 <= waiting_time < 6:
                for op_user_id, op_user_from in waiting_list:
                    gap = abs(user_info_list[user_id-1]['grade'] - user_info_list[op_user_id-1]['grade'])
                    if gap < 600:
                        match_commands.append([user_id, op_user_id])
                        user_play_count[user_id] += 1
                        user_play_count[op_user_id] += 1
                        matched.append(op_user_id)
                        break
            elif 6 <= waiting_time < 8:
                for op_user_id, op_user_from in waiting_list:
                    gap = abs(user_info_list[user_id-1]['grade'] - user_info_list[op_user_id-1]['grade'])
                    if gap < 800:
                        match_commands.append([user_id, op_user_id])
                        user_play_count[user_id] += 1
                        user_play_count[op_user_id] += 1
                        matched.append(op_user_id)
                        break
            elif 8 <= waiting_time < 10:
                for op_user_id, op_user_from in waiting_list:
                    gap = abs(user_info_list[user_id-1]['grade'] - user_info_list[op_user_id-1]['grade'])
                    if gap < 1000:
                        match_commands.append([user_id, op_user_id])
                        user_play_count[user_id] += 1
                        user_play_count[op_user_id] += 1
                        matched.append(op_user_id)
                        break
            else:
                for op_user_id, op_user_from in waiting_list:
                    match_commands.append([user_id, op_user_id])
                    user_play_count[user_id] += 1
                    user_play_count[op_user_id] += 1
                    matched.append(op_user_id)
                    break
        
        a=match(auth_key, match_commands)

        
    a=match(auth_key, [])
    print(score(auth_key))

p1_simulator()


