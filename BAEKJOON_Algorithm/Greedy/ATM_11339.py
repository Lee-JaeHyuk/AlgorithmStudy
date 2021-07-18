n = int(input())

s = list(map(int,input().split()))
s.sort()
sum = 0
k = len(s)
for i in range(0,len(s)):
    t = s[i]*k
    sum+=t
    k = k-1
print(sum)