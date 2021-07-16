# 상하좌우로 움직이는 여행가

m = int(input())

data = input().split()
x, y = (1, 1)

for i in range(0, len(data)):
    if data[i] == 'L':
        if y == 1:
            continue
        else:
            y -= 1
    elif data[i] == 'R':
        if y == len(data):
            continue
        else:
            y += 1
    elif data[i] == 'U':
        if x == 1:
            continue
        else:
            x -= 1
    elif data[i] == 'D':
        if x == len(data):
            continue
        else:
            x += 1
print(x, y)
