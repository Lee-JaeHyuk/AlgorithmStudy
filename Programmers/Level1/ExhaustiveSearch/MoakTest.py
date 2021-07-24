def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]

    for i in range(0, len(answers)):
        if answers[i] == a1[i%5]:
            answer[0] += 1
        if answers[i] == a2[i%8]:
            answer[1] += 1
        if answers[i] == a3[i%10]:
            answer[2] += 1
    mx = answer[0]
    re = []
    re.append(1)
    if mx < answer[1]:
        mx = answer[1]
        re.clear()
        re.append(2)
    elif mx == answer[1]:
        re.append(2)
    if mx < answer[2]:
        re.clear()
        re.append(3)
    elif mx == answer[2]:
        re.append(3)
    '''
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    enumerate 개념 이해하기
    '''
    return re
