
# 아이디어:
#  안 마시는 경우를 기점으로 나눈다.
#  3잔 연속 마시는 경우가 생기지 않도록, dp 불러온 후에는 안 마시는 경우를 반드시 넣고 간다.

# dp[n]: n번까지 진행했을 때의 최댓값
# 3가지 경우가 존재
# 1. 현재 포도주 마시지 않는 경우: dp[n-1] 
# 2. 현재 포도주 마시는 경우
#   2-1. n-2 안 마시고, n-1마시고, 현재 마시기: dp[n-3]+arr[n-1]+arr[n]
#   2-2. n-1 안 마시고, 현재 마시기

# dp[n-1]                              dp x
# dp[i-3] + array[i] + array[i-1]  dp x o o
# dp[i-2] + array[i]                 dp x o 

import sys

read = sys.stdin.readline

n = int(read())
arr = [int(read()) for _ in range(n)]
if (n == 1):
    print(arr[0])
    exit(0)
elif(n == 2):
    print(arr[0] + arr[1])
    exit(0)

dp = [ 0 for i in range(n)]
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], dp[1], arr[1] + arr[2])
for i in range(3, len(arr)):
    dp[i] = max(
        dp[i-1],
        dp[i-3] + arr[i-1] + arr[i],
        dp[i-2] + arr[i]
    )

print(dp[n-1])