'''idea
https://www.acmicpc.net/problem/1162
도로포장

시작: 21.11.18 03:39

dp[i][k] = 포장할 도로의 수가 k개 이하이고, 경로 i가 추가되었을 때의 최소 시간

포장 도로 개수

                          k = 0   k = 1   k = 2   k = 3
경로 1만 있을 때
[10, 10]                   20      10       0       0

경로 1, 2 모두 있을 때
[10, 10],               [i-1][0]  min([i-1][0], 현재에서 max 지우기)
[1, 100]                  20        1



[정답]
https://wookcode.tistory.com/m/156?category=1008519
https://wookkl.tistory.com/28
 dist[i][k] : 시작점에서 i까지 k개 도로를 포장하여 가는 최단 경로 cost

'''
import sys
import heapq
sys.setrecursionlimit(10**9)

read = sys.stdin.readline
n, m, k = map(int, read().split())
graph = [dict() for _ in range(n)]
# print(graph)

for i in range(m):
    a, b, w = map(int, read().split())
    a -= 1
    b -= 1
    graph[a][b] = w
    graph[b][a] = w
    # print("\n".join(str(row) for row in graph))

# print("\n".join(str(row) for row in graph))

route = []
frm, to = 0, 0


path = []
visited = [0] * n
visited[0] = 1


# dp[i][k] = 포장할 도로의 수가 k개 이하이고, 경로 i가 추가되었을 때의 최소 시간
dp = [0] * (k+1)



is_first = True



def get_path(frm, visited, route):
    if frm == n-1:
        # path.append(route[:]) # 배열
        # path.append(route) # max heap

        # route에 대해 로직 실행
        global is_first
        global dp
        if is_first:
            # 초기값
            for i in range(k+1):
                dp[i] = sum(route)
                if route:
                    heapq.heappop(route)
            is_first = False
        else:
            for i in range(1, k+1):
                if route:
                    heapq.heappop(route)
                # print(f"이전, 현재 = {dp[i]}, {sum(route)}")
                dp[i] = max(dp[i], sum(route))


    for to in graph[frm].keys():
        if visited[to] == 0:
            visited[to] = 1
            # 경로 확인용
            # route.append([to, graph[frm][to]])

            # ~~~ 그냥 배열 사용
            # route.append(graph[frm][to])
            # get_path(to, visited, route)
            # route.pop()
            # visited[to] = 0

            # ~~~ max heap
            tmp = route[:]
            heapq.heappush(tmp, -graph[frm][to])
            get_path(to, visited, tmp)
            visited[to] = 0
            

get_path(0, visited, [])
print(dp[-1] * (-1))

