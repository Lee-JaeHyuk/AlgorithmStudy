def solution(nums):
    sol = 0
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                num = nums[i]+nums[j]+nums[k]
                if search(num) == True:
                    sol += 1
    return sol


def search(num):
    cout = 0
    for i in range(2, num):
        if num % i == 0:
            cout += 1
    if cout == 0:
        return True
    else:
        return False

# combination 함수 이용해보기
