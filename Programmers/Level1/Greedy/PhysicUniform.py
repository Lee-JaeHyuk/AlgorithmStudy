def solution(n, lost, reserve):
    a = set(lost) - set(reserve)
    b = set(reserve) - set(lost)
    for i in b:
        if i-1 in a:
            a.remove(i-1)
        elif i+1 in a:
            a.remove(i+1)
    answer = n - len(a)
    return answer


n = 5
lost = [2,4]
reverse = [1,3,5]

print(solution(n, lost, reverse))
