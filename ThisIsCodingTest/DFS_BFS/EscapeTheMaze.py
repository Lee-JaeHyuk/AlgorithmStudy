from collections import deque

# 미로 탈출 (BFS)

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for j in range(4):
            mx = x + move_x[j]
            my = y + move_y[j]
            if mx < 0 or mx > n - 1 or my < 0 or my > m - 1:
                continue
            if graph[mx][my] == 0:
                continue
            if graph[mx][my] == 1:
                graph[mx][my] = graph[x][y] + 1
                queue.append((mx, my))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
