from collections import deque

# 특정 거리의 도시 찾기 (BFS)

n, m, k, x = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b)

distance = [-1] * n
distance[x-1] = 0

queue = deque()
queue.append(x)
while queue:
    nx = queue.popleft()
    for next_step in graph[nx-1]:
        if distance[next_step-1] == -1:
            distance[next_step -1] = distance[nx-1] + 1
            queue.append(next_step)

answer = []

for i in range(len(distance)):
    if k == distance[i]:
        answer.append(i+1)
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])