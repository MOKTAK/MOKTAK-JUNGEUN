'''idea

'''
import sys

read = sys.stdin.readline

N, Q = list(map(int, read().split()))
arr = list(map(int, read().split()))

queue = [0 for _ in range(Q)]

[]

for i in arr:
    for j in range(Q):
        if Q[j][-1] < i:
            Q[j].append(i)
            break


# print(' '.join(map(str,arr)) + '\n')