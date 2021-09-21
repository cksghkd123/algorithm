import requests

x_auth_token = '71d33c37335cc26cf16774f766f34385'

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

    print(locations(BASE_URL, auth_key))
    print(trucks(BASE_URL, auth_key))
    commands = [
        {"truck_id": 0, "command": [1, 1]},
        {"truck_id": 1, "command": [2, 1, 1]},
        {"truck_id": 2, "command": [2, 2, 1, 1]},
        {"truck_id": 3, "command": [2, 2, 2, 1, 1]},
        {"truck_id": 4, "command": [2, 2, 2, 2, 1, 1]}
    ]

    simulate(BASE_URL, auth_key, commands)
    print(locations(BASE_URL, auth_key))
    print(trucks(BASE_URL, auth_key))

    


p1_simulator()
