'''idea
https://www.acmicpc.net/problem/12865

골드 5

시작: 21.11.16 22:03




2차원 dp


weight, value

row: 물건이 하나씩 늘어남
column: 가방 최대 용량이 1씩 늘어남
dp[r][c]: r번째 물건까지 사용할 때, 가방 용량이 c일 때의 최대 가치

item = [[weight, value]]

1) 만약 x-(r의 weight) >= 0:
    dp[r][x] = max(dp[r-1][x-(r의 weight)] + r의 value, dp[r-1][x])
2) else:
    // 현재 물건을 안 넣는 경우
    dp[r][x] = dp[r-1][x]


# ~~~ 다른 사람 풀이
# https://www.acmicpc.net/source/32887589
# dp를 k부터 -1 하면서 돌아서 tmp를 안 만들어도 된다.
# 끝나는 지점을 w-1로 해서 0 부분은 아예 계산을 안 한다.

'''

# # ~~~ 2차원 배열: 시간초과
# import sys
# read = sys.stdin.readline
# n, k = map(int, read().split())

# # weight, value의 인덱스
# w, v = 0, 1
# item = [tuple(map(int, read().split())) for _ in range(n)]
# item.sort()
# dp = [[0 for _ in range(k+1)] for _ in range(n)]

# # 초기값
# for i in range(item[0][w], k+1):
#     dp[0][i] = item[0][v]

# for i in range(1, n):
#     for j in range(k+1):
#         if j-item[i][w] >= 0:
#             dp[i][j] = dp[i-1][j-item[i][w]] + item[i][v]
        
#         dp[i][j] = max(dp[i-1][j], dp[i][j])
# print(dp[-1][-1])
# # print("\n".join(str(row) for row in dp))





# ~~~ 1차원 배열
import sys
read = sys.stdin.readline
n, k = map(int, read().split())

# weight, value의 인덱스
w, v = 0, 1
item = [tuple(map(int, read().split())) for _ in range(n)]
# item.sort()
dp = [0 for _ in range(k+1)]

# 초기값
for i in range(item[0][w], k+1):
    dp[i] = item[0][v]

for i in range(1, n):
    tmp = dp[:]
    for j in range(k+1):
        if j-item[i][w] >= 0:
            dp[j] = max(tmp[j-item[i][w]] + item[i][v], tmp[j])
    # print(dp)
print(dp[-1])



# # ~~~ 다른 사람 풀이
# # https://www.acmicpc.net/source/32887589
# # dp를 k부터 -1 하면서 돌아서 tmp를 안 만들어도 된다.
# # 끝나는 지점을 w-1로 해서 0 부분은 아예 계산을 안 한다.
# N,K = map(int, input().split())
# things = []

# for _ in range(N):
#     w,v = map(int, input().split())
#     things.append((w,v))
    
# dp = [0]*(K+1)

# for w,v in things:
#     for i in range(K, w-1, -1):
#         dp[i] = max(dp[i], dp[i-w]+v)
        
# print(dp[-1])