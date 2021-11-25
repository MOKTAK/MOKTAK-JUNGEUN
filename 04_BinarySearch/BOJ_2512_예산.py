'''idea
https://www.acmicpc.net/problem/2512
예산

시작: 21.11.23 22:22
  끝: 21.11.23 22:41


'''
import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
m = int(read())

mx = 0
result = 0

left, right = 0, max(arr)
while (left <= right):
    mid = (left + right)//2
    sum = 0
    for i in arr:
        if i - mid > 0:
            sum += (mid)
        else:
            sum += i
    if sum == m:
        mx = max(mx, mid)
        break 
    elif sum < m:
        mx = max(mx, mid)
        left = mid+1
    else:
        right = mid-1
print(mx)
