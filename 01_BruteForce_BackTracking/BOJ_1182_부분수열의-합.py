'''idea
https://www.acmicpc.net/problem/1182

시작: 21.11.04 12:45
끝: 21.11.04 13:00

1) S에서 빼가면서 찾기

부분수열-> 연속적인 값이 아니어도 된다.

2) combination으로 뽑고 더하기

'''
# import sys
# import collections


# read = sys.stdin.readline


# N, S = list(map(int, read().split()))
# arr = list(map(int, read().split()))

# count = 0
# for i in range(0, N-1):
#     sum = S-arr[i]
#     for j in range(i+1, N):
#         sum -= arr[j]
#         if sum == 0:
#             count += 1

# if arr[-1] == S:
#     count += 1
# print(count)


from itertools import combinations
import sys
import collections


read = sys.stdin.readline


N, S = list(map(int, read().split()))
arr = list(map(int, read().split()))

count = 0
for i in range(1, N+1):
    for j in combinations(arr, i):
        if sum(list(j)) == S:
            count += 1
print(count)