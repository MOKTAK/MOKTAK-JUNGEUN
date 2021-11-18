'''idea
https://www.acmicpc.net/problem/10844
쉬운 계단 수



시작 : 21.11.16 00:00
  끝 : 21.11.16 00:30


실버1

~~~아이디어 1 : 틀림
dp[i]: 길이가 i인 계단 수의 개수
dp[2] = dp[1]*2 -1   // 마지막 -1은 9보다 큰 숫자가 없기 때문에 생긴다.

dp[i] = dp[i-1]*2 -2 // 9다 큰 숫자, 0보다 작은 숫자 제외


~~~ 아이디어 2
규칙: 9와 0으로 끝나는 애들은 *1로 간다.
      8과 1로 끝나는 애들은 9와 0으로 끝나는 애들을 만든다.
    ..

dp에 idx에 해당하는 숫자로 끝나는 계단수의 개수를 넣는다.

'''

import sys
read = sys.stdin.readline

n = int(read())

# 각 숫자로 끝나는 계단수의 개수
dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for j in range(1, n):
    tmp = dp[:]
    dp[0] = tmp[1]
    dp[9] = tmp[8]
    for i in range(1, 9):
        dp[i] = tmp[i-1] + tmp[i+1]

print(sum(dp)%1000000000)