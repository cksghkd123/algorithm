import collections

n, k, c = map(int, input().split())

all_teams_info = []
rank_map = {} 
for i in range(n):
    team_id, school_id = map(int, input().split())
    all_teams_info.append((team_id, school_id))
    rank_map[team_id] = i

answer = []
teams_count = collections.defaultdict(int)
candidate_teams = collections.deque()

for team_id, school_id in all_teams_info:
    if teams_count[school_id] < c:
        teams_count[school_id] += 1
        answer.append(team_id)
    else:
        candidate_teams.append(team_id)

while len(answer) < k:
    answer.append(candidate_teams.popleft())

answer.sort(key=lambda team_id: rank_map[team_id])

for i in range(k):
    print(answer[i])
