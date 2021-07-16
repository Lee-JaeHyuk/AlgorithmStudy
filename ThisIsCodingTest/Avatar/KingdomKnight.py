# 체스 왕실의 나이트

n = input()

move = [(-2,-1), (-2,1), (2 ,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

row = int(n[1])
col = ord(n[0]) - ord('a') + 1

count = 0

data = (row,col)

for step in move:
    print(step, data)
    next_step = step + data
    if next_step[0] > 8 or next_step[0] <1:
        continue
    elif next_step[1] > 8 or next_step[1] <1:
        continue
    else:
        count += 1

print(count)
