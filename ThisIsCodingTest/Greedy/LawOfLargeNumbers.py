# 큰수의 법칙

# 1번 풀이

n, m, k = map(int, input().split())

dataList = list(map(int, input().split()))

dataList.sort()
dataList.reverse()

count = 0
sum = 0

while m:
    if(count < k):
        sum += dataList[0]
        count += 1
    else:
        sum += dataList[1]
        count = 0
    m -= 1

print(sum)

# 2번 풀이

n, m, k = map(int, input().split())

dataList = list(map(int, input().split()))

dataList.sort()
dataList.reverse()

first = dataList[0]
second = dataList[1]

count = int(m/(k+1)) * k
count =+ m % (k+1)

result = (first * count) + (second * (m-count))
print(result)