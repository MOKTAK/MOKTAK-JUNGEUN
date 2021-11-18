'''idea
https://www.acmicpc.net/problem/1149
RGB거리

시작 21.11.18 03:12
  끝 21.11.18 03:24

[아이디어]
dp = [r, g, b]
dp[color]: 현재 집을 color로 칠했을 때의 비용의 최솟값

dp = [r, g, b]
dp[0] = min(dp[1], dp[2]) + r로 칠했을 때의 비용

'''

import sys
read = sys.stdin.readline

n = int(read())
cost = [list(map(int, read().split())) for _ in range(n)]
dp = cost[0][:]
tmp = []
for i in range(1,n):
    tmp = dp[:]
    for color in [0, 1, 2]:
        dp[color] = min(tmp[(color+1)%3], tmp[(color+2)%3]) + cost[i][color]
print(min(dp))
