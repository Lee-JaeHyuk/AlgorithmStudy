
a = int(input())

t = []
for i in range(a):
    t.append(int(input()))

t.sort()
t.reverse()

for i in t:
    print(i, end=' ')

