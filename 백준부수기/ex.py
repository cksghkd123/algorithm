def change_sec(time):
	hh, mm, ss = map(int,time.split(':'))
	result = hh*3600 + mm*60 + ss*1
	return result

def solution(play_time, adv_time, logs):
	play_time = change_sec(play_time)
	adv_time = change_sec(adv_time)

	time_line = [(0, 0), (play_time, 0)]
	for l in logs:
		s, e = l.split('-')
		n_s = change_sec(s)
		time_line.append((n_s, 1))
		n_e = change_sec(e)
		time_line.append((n_e, -1))
	time_line.sort()

	m = 0
	v_time_line = []
	for i, j in time_line:
		m += j
		v_time_line.append((i, m))
	
	answer = (0, 0)
	for i in range(len(v_time_line)-1):
		watching_time = 0
		time_remaining = adv_time
		num = v_time_line[i][1]
		for j in range(i+1, len(v_time_line)):
			gap = v_time_line[j][0] - v_time_line[j-1][0]
			if time_remaining > gap:
				watching_time += num*gap
				time_remaining -= gap
			else:
				watching_time += num*time_remaining
				time_remaining = 0
				break
			num = v_time_line[j][1]

		if watching_time == answer[0]:
			continue
		answer = max(answer, (watching_time,v_time_line[i][0]))
	
	for i in range(len(v_time_line)-1,0,-1):
		watching_time = 0
		time_remaining = adv_time
		num = v_time_line[i-1][1]
		for j in range(i-1, -1, -1):
			gap = v_time_line[j+1][0] - v_time_line[j][0]
			if time_remaining > gap:
				watching_time += num*gap
				time_remaining -= gap
			else:
				watching_time += num*time_remaining
				time_remaining = 0
				break
			if j == 0:
				break
			num = v_time_line[j-1][1]
		
		if watching_time == answer[0] and v_time_line[i][0] - adv_time > answer[1]:
			continue
		answer = max(answer, (watching_time, v_time_line[i][0]-adv_time))


	hh = answer[1]//3600
	mm = (answer[1]%3600)//60
	ss = (answer[1]%3600)%60
	answer = "{:02d}:{:02d}:{:02d}".format(hh,mm,ss)
	return answer




a = "02:03:55"
b = "00:14:15"	
c = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(a, b, c))