def solution(record):
    answer = []
    for i in record:
        x = i.split()
        if x[0] == 'Enter' or x[0] == 'Change':
            answer.append(i)
            for j in range(len(answer)):
                y = answer[j].split()
                if len(y) == 3:
                    if y[1] == x[1]:
                        y[2] = x[2]
                    answer[j] = ' '.join(y)
        else:
            answer.append(i)
    for i in range(len(answer)):
        x = record[i].split()
        if x[0] == 'Leave':
            x.append('a')
            for j in answer:
                y = j.split();
                if len(y) == 3:
                    if y[1] == x[1]:
                        x[2] = y[2]
                        #print(x,i,j)
                        answer[i] = ' '.join(x)
    result = []
    for i in answer:
        t = i.split()
        if t[0] == 'Enter':
            result.append(t[2] + "님이 들어왔습니다")
        elif t[0] == 'Leave':
            result.append(t[2] + "님이 나갔습니다")
    return result
# 시간초과 / 노가다
rec = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(rec))


