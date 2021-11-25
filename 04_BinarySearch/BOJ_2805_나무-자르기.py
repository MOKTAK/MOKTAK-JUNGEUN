'''idea




최대높이

가운데 자름
나무 합 구함

나무 합 = M
합<M:


'''
import sys
import collections

read = sys.stdin.readline
print= sys.stdout.write

N, M = map(int,read().split())
arr = list(map(int, read().split()))

max_height = max(arr)

answer = 0

start , end = 0, max_height

height_sum = 0

