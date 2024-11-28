def parse_time(time):
	h, m, s = map(int, time.split(':'))
	
	return h*3600 + m*60 + s

def print_status(status):
	if log_storage[status]:
		print(f'{status}:')
		for log in log_storage[status]:
			print_log(log)
		
		print()
		
def print_log(log):
	if log.repeat == 1:
		print(f'- {log.time} {log.comment}')
	else:
		print(f'- {log.time} {log.comment} (x{log.repeat})')
		
def is_continuous(status, comment):
	if log_storage[status]:
		prev_log = log_storage[status][-1]
		if prev_log.comment == comment:
			return True
	
	return False

def is_matched(comment, keyword):
	return keyword.lower() in comment.lower()

	
class Log:
	def __init__(self, time, comment):
		self.time = time
		self.comment = comment
		self.repeat = 1
	
	
start_time, end_time, keyword = input().split()
start_time = parse_time(start_time)
end_time = parse_time(end_time)

n = int(input())

status_list = ['[INFO]', '[WARN]', '[ERROR]']

log_storage = {'[INFO]': [], '[WARN]': [], '[ERROR]': []}
is_logged = False

for _ in range(n):
	time, status, *comment = input().split()
	
	comment = ' '.join(comment)
	parsed_time = parse_time(time)
	if parsed_time < start_time:
		continue
	
	if parsed_time > end_time:
		break
	
	if is_matched(comment, keyword):
		is_logged = True
		
		if is_continuous(status, comment):
			log_storage[status][-1].repeat += 1
		else:
			log_storage[status].append(Log(time, comment))
		

if is_logged:
	for status in status_list:
		print_status(status)
else:
		print('No logs found.')


