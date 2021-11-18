'''idea
https://www.acmicpc.net/problem/2579
계단 오르기

시작: 21.11.18 04:58
  끝: 21.11.18 05:19

[아이디어]
dp[i]: 현재 계단을 밟았을 때, 현재 계단까지의 최대 점수
p[i]: i번째 계단의 점수

? o x o o
? ? o x o

dp[i] = max(dp[i-3]+ p[i-1], dp[i-2]) + p[i]





'''
import sys

read = sys.stdin.readline

n = int(read())
dp3 = int(read())
if n == 1:
    print(dp3)
    exit(0)

p_before = int(read())
dp2 = dp3 + p_before
if n == 2:
    print(dp2)
    exit(0)

p_now = int(read())
dp1 = max(dp3, p_before) + p_now

p_before = p_now
for _ in range(3, n):
    p_now = int(read())
    tmp = max(dp3+ p_before, dp2) + p_now
    dp3, dp2, dp1 = dp2, dp1, tmp
    p_before = p_now

print(dp1)