def solution(a, b):
    sum = 0
    for i in range(0,len(a)):
        sum += a[i]*b[i]
    return sum

#zip을 이용한 풀이
#list = sum([x*y for x,y in(a,b)])