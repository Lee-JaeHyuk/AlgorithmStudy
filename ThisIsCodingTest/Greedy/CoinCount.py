# 거스름돈 계산
n = int(input())

list = [500, 100, 50, 10]

count = 0

for coin in list:
    count += n//coin
    n %= coin
print(count)