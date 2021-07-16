# 1이 될 때까지

n, k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break
    elif n % k == 0:
        count += 1
        n = n//k
    else:
        count += 1
        n = n - 1
print(count)
