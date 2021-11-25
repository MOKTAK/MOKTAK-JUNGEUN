'''
https://www.acmicpc.net/problem/2110
공유기 설치

나중에 다시 풀기~

시작: 21.11.25 16:39
끝: 21.11.25 18:26

공유기 사이의 거리를 mid로 두어 이분탐색
-> 틀림.. 근데 왜 틀렸는지 모르겠음

참고: 다른 사람 풀이
https://assaeunji.github.io/python/2020-05-07-bj2110/


'''


import sys
read = sys.stdin.readline

n, c = map(int, read().split())
arr = [int(read()) for _ in range (n)]
arr.sort()
dist = [ arr[i+1] - arr[i] for i in range(len(arr)-1)]

result = 0
# 공유기 사이의 거리 최솟값, 최댓값
left, right = min(dist), max(dist)
while left <= right:
    # 가장 인접한 두 공유기 사이의 거리
    mid = (left + right) // 2
    count = 1
    sum = 0
    # 실제로 mid만큼의 거리가 있었는지
    check = False 
    for i in dist:
        sum += i
        if sum >= mid:
            if sum == mid:
                check = True
            count += 1
            sum = 0
            

    if count == c and check:
        result = mid
        left = mid + 1
    elif count < c:
        right = mid-1
    else:
        left = mid+1

print(result)