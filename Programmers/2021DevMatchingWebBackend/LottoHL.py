def solution(lottos, win_nums):
    r = [6,6,5,4,3,2,1]
    answer = 0
    onum = 0
    for i in lottos:
        if i == 0:
            onum += 1
            continue
        for j in win_nums:
            if i == j:
                answer += 1
    result = []
    bad = answer
    luk = answer + onum
    result.append(r[luk])
    result.append(r[bad])
    return result

