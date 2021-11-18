'''idea
https://www.acmicpc.net/problem/2293
동전 1

실버 1

시작: 21.11.16 12:32

~~~ 아이디어1



dp[i]: i원이 되도록 하는 모든 경우의 수 (set)

for 동전 개수:
    dp[i] = dp[i] + dp[i-arr[j]]

=> 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다. 이 조건에 안 맞음



~~~ 정답 해설
https://debuglog.tistory.com/78
배낭문제랑 비슷하게 풀이해야 한다..

d[i][k]: i번째 동전까지 사용했을때, k를 만들 수 있는 경우의 수

c[i]: i번째 동전의 가치

1) 만약 k-c[i] > 0이라면
    # 현재 동전까지 사용하는 경우의 수 + 동전이 하나 부족한 개수일 떄 해결하는 경우의 수
    d[i][k] = d[i][k-c[i]] + d[i-1][k]
2) k-c[i] > 0 이 아니라면
    d[i][k] = d[i-1][k]

첫번째 동전에 대하여
d[i][c[1]] = 1
k-c[1]가 0보다 크다면 
d[1][k] = d[1][k-c[1]] + 1


시사점:
물건들을 이용해 어떤 값을 채워야 하는 문제가 나오면, 
(물건을 하나씩 더 추가하며 경우의 수를 나눌 수 있고, 어떤 값을 채워야 한다면)
배낭문제처럼 2차원 배열을 만들자.

'''
# import sys
# read = sys.stdin.readline

# n, k = map(int, read().split())
# arr = [int(read()) for _ in range(n)]

# dp = [0 for i in range(k+1)]
# for i in range(n):
#     dp[arr[i]] = 1

# # i: 만들고자 하는 금액
# for i in range(k+1):
#     for j in range(n):
#         # arr[j]: 현재 계산중인 동전
#         if (i-arr[j] > 0):
#             dp[i] = dp[i]
#         print(f"{i}원 만들기, 동전 = {arr[j]}, {dp}")

# print(dp[k])


import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coin = [int(read()) for _ in range(n)]
# dp[n] = 금액이 n일때의 경우의 수
dp = [0 for j in range(k+1)]


coin.sort()
# 불가능한 경우
if (coin[0] > k):
    print(0)
    exit()

# 첫 번째 동전 초기화
dp[0] = 1
dp[coin[0]] = 1
for i in range(coin[0]+1, k+1):
    dp[i] = dp[i-coin[0]]

# 나머지 계산
for c in range(1, n):
    for v in range(k+1):
        if (v - coin[c]) >= 0:
            dp[v] += dp[v-coin[c]] 

print(dp[k])


# ~~~ 2차원 dp: 메모리 초과
# for c in range(2, n+1):
#     for v in range(k+1):
#         dp[c][v] = dp[c-1][v]
#         if (v-coin[c]) >= 0:
#             # print(f"c = {c}, v = {v}, {dp[c-1][v]}, {dp[c][v-coin[c]]}")
#             dp[c][v] += dp[c][v-coin[c]] 
#             # print("\n".join([" ".join([str(i) for i in row]) for row in dp]))
# print("\n".join([" ".join([str(i) for i in row]) for row in dp]))
