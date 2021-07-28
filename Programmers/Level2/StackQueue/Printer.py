def solution(priorities, location):
    ml = [0 for x in priorities]
    ml[location] = 1
    count = 1
    while True:
        t = priorities[0]
        s = ml[0]
        cnt = 0
        for i in priorities:
            if i > t:
                cnt += 1
        if cnt > 0:
            del priorities[0]
            del ml[0]
            priorities.append(t)
            ml.append(s)
        else:
            if ml[0] == 1:
                return count
            else:
                count +=1
                del priorities[0]
                del ml[0]
    answer = 0
    return answer


p = [2,1,3,2]
loc = 2
#print(solution(p,loc))

#2 enumerate 함수를 사용

def sol(pro, loc):
    answer = 0
    ls = [(i,m) for i,m in enumerate(pro)]

    while True:
        cur = ls.pop(0)
        for t in ls:
            if cur[1] < t[1]:
                ls.append(cur)
            else:
                answer += 1
                if cur[0] == loc:
                    return answer

print(sol(p,loc))



