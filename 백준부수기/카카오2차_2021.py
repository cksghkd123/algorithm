import requests

x_auth_token = '2ee9d3f67f34fba8d35e35d1ddb485fc'

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'

def start(url, x_auth_token, number):
    uri = url + '/start'
    
    return requests.post(uri, headers={'X-Auth-Token': x_auth_token}, json={'problem': number}).json()

def locations(url, auth_key):
    uri = url + '/locations'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

def trucks(url, auth_key):
    uri = url + '/trucks'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

def simulate(url, auth_key, commands):
    uri = url + '/simulate'

    return requests.put(uri, headers={'Authorization': auth_key}, json={'commands': commands}).json()

def score(url, auth_key):
    uri = url + '/score'

    return requests.get(uri, headers={'Authorization': auth_key}).json()

# 0: 6초간 아무것도 하지 않음
# 1: 위로 한 칸 이동
# 2: 오른쪽으로 한 칸 이동
# 3: 아래로 한 칸 이동
# 4: 왼쪽으로 한 칸 이동
# 5: 자전거 상차
# 6: 자전거 하차

def p1_simulator():
    auth_key = start(BASE_URL, x_auth_token, 1)['auth_key']

    commands = [
        {"truck_id": 0, "command": []},
        {"truck_id": 1, "command": []},
        {"truck_id": 2, "command": []},
        {"truck_id": 3, "command": []},
        {"truck_id": 4, "command": []}
    ]
    simulate(BASE_URL, auth_key, commands)

    for i in range(719):
        # commands = []
        # locations_info = locations(BASE_URL, auth_key)['locations']
        # trucks_info = trucks(BASE_URL, auth_key)['trucks']

        # for j in range(5):
        #     truck_location = trucks_info[j]['location_id']
        #     loaded_bike_count = trucks_info[j]['loaded_bikes_count']
        #     commands1 = []
        #     commands2 = []

        #     if i%2 == 0:
        #         for k in range(3):
        #             loaded_bike_count += locations_info[truck_location+k]['located_bikes_count']
        #         if loaded_bike_count%3 == 0:
        #             target_count = [loaded_bike_count//3] *3
        #         elif loaded_bike_count%3 == 1:
        #             target_count = [loaded_bike_count//3+1, loaded_bike_count//3, loaded_bike_count//3]
        #         elif loaded_bike_count%3 == 2:
        #             target_count = [loaded_bike_count//3+1, loaded_bike_count//3+1, loaded_bike_count//3]
                
        #         for k in range(3):
        #             if locations_info[truck_location+k]['located_bikes_count'] < target_count[k]:
        #                 commands1.append(1)
        #                 commands2.append(3)
        #                 for _ in range(target_count[k] - locations_info[truck_location+k]['located_bikes_count']):
        #                     commands2.append(6)
        #             elif locations_info[truck_location+k]['located_bikes_count'] == target_count[k]:
        #                 commands1.append(1)
        #                 commands2.append(3)
        #             elif locations_info[truck_location+k]['located_bikes_count'] > target_count[k]:
        #                 for _ in range(locations_info[truck_location+k]['located_bikes_count'] - target_count[k]):
        #                     commands1.append(5)
        #                 commands1.append(1)
        #                 commands2.append(3)
        #         commands2.reverse()
        #         commands1.pop()
        #         commands2.pop()
        #         command = commands1 + commands2

        #     elif i%2 == 1:
        #         for k in range(3):
        #             loaded_bike_count += locations_info[truck_location-k]['located_bikes_count']
        #         if loaded_bike_count%3 == 0:
        #             target_count = [loaded_bike_count//3] *3
        #         elif loaded_bike_count%3 == 1:
        #             target_count = [loaded_bike_count//3+1, loaded_bike_count//3, loaded_bike_count//3]
        #         elif loaded_bike_count%3 == 2:
        #             target_count = [loaded_bike_count//3+1, loaded_bike_count//3+1, loaded_bike_count//3]
                
        #         for k in range(3):
        #             if locations_info[truck_location-k]['located_bikes_count'] < target_count[k]:
        #                 commands1.append(3)
        #                 commands2.append(1)
        #                 for _ in range(target_count[k] - locations_info[truck_location-k]['located_bikes_count']):
        #                     commands2.append(6)
        #             elif locations_info[truck_location-k]['located_bikes_count'] == target_count[k]:
        #                 commands1.append(3)
        #                 commands2.append(1)
        #             elif locations_info[truck_location-k]['located_bikes_count'] > target_count[k]:
        #                 for _ in range(locations_info[truck_location-k]['located_bikes_count'] - target_count[k]):
        #                     commands1.append(5)
        #                 commands1.append(3)
        #                 commands2.append(1)
        #         commands2.reverse()
        #         commands1.pop()
        #         commands2.pop()
        #         command = commands1 + commands2

        #     commands.append({"truck_id": j, "command": command})

        print(i)
        simulate(BASE_URL, auth_key, commands)       

    print(score(BASE_URL, auth_key))


p1_simulator()