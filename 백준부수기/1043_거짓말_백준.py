def donlie(party_number,  count):
    if party_number == m:
        global answer
        answer = max(answer, count)
        return


    mosson = 0
    for i in participant[party_number]:
        if truth_button[i] == -1:
            if mosson == 1:
                return
            mosson = -1
        elif truth_button[i] == 1:
            if mosson == -1:
                return
            mosson = 1

    else:
        if mosson == 1:
            #진실을 말함
            being_truth = []
            for i in participant[party_number]:
                if truth_button[i] == 0:
                    being_truth.append(i)
                    truth_button[i] = 1        
            donlie(party_number+1, count)
            for i in being_truth:
                truth_button[i] = 0
        
        elif mosson == 0:
            #진실을 말함
            for i in participant[party_number]:
                truth_button[i] = 1        
            donlie(party_number+1, count)
            for i in participant[party_number]:
                truth_button[i] = 0

            #거짓을 말함
            for i in participant[party_number]:
                truth_button[i] = -1       
            donlie(party_number+1, count+1)
            for i in participant[party_number]:
                truth_button[i] = 0

        elif mosson == -1:
            #거짓을 말함
            being_false = []
            for i in participant[party_number]:
                if truth_button[i] == 0:
                    being_false.append(i)
                    truth_button[i] = -1        
            donlie(party_number+1, count+1)
            for i in being_false:
                truth_button[i] = 0


answer = 0
n, m = map(int,input().split())
truth_button = [0 for _ in range(n+1)]
init_truth = list(map(int,input().split()))
init_truth.pop(0)
for i in init_truth:
    truth_button[i] = 1

participant = []
for i in range(m):
    participant.append(list(map(int,input().split())))
    participant[i].pop(0)


donlie(0, 0)
print(answer)

