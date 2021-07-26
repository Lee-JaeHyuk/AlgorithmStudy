# 효울성 테스트 실패
def solution(s):
    index = 0
    ls = list(s)
    i = 0
    while True:
        if len(ls) == 1:
            return 0
        if len(ls) == 0:
            return 1
        if index == len(ls)-1:
            return 0
        if ls[index] == ls[index+1]:
            del ls[index]
            del ls[index]
            index = 0
        else:
            index += 1
        i += 1
    return answer

def solution2(s):
    st = []
    for i in s:
        if len(st) == 0:
            st.append(i)
        elif st[-1] == i:
            st.pop()
        else:
            st.append(i)
    if len(st) == 0:
        return 1
    else:
        return 0


print(solution2("baabbaac"))