def solution(left, right):
    sum = 0
    for i in range(left,right+1):
        if search(i) == True:
            sum += i
        else:
            sum -= i
    return sum

# 제곱수는 약수의 갯수가 홀수이다. 그걸 이용하면 좀 더 쉽게 풀이가 가능하다

def search(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt%2 == 0:
        return True
    else:
        return False