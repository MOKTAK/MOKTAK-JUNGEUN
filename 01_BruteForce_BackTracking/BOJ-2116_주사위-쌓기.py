'''idea
https://www.acmicpc.net/problem/2116

시작: 21.11.04 13:05 
끝: 21.11.04 13:37

1)
a-f, b-d, c-e는 짝꿍(0-5, 1-3, 2-4)
3가지 경우에 대해 모두 계산

1) a-f 짝의 열을 제외한 모든 열 중 최댓값의 합
2) b-d 이하 같음
3) 마찬가지

1, 2, 3중 최댓값
=>틀림 (주사위마다 숫자가 달라지면서 헤아려야 하는 짝꿍도 달라짐)

2)
1번주사위의 모든 면이 바닥이 되게 해보고, 그 중 최댓값 선택
'''
# import sys
# import collections

# read = sys.stdin.readline
# # print= sys.stdout.write

# N = int(read())
# arr = [list(map(int, read().split())) for i in range(N)]


# print(' '.join(map(str, arr)) + '\n')

# case = [[0, 5], [1, 3], [2, 4]]

# max_case = 0
# for c in case:
#     current_max = 0
#     for i in range(N):
#         dice_side = arr[i][:]
#         print(dice_side)
#         print(f"{c[0]}, {c[1]}")

#         del dice_side[c[0]]
#         del dice_side[c[1]-1]

#         max_num = max(dice_side)
#         print(max_num)
#         current_max += max_num
#     max_case = max(max_case, current_max)


import sys
import collections

read = sys.stdin.readline
# print= sys.stdout.write

N = int(read())
arr = [list(map(int, read().split())) for i in range(N)]

back = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

max_case = 0
# 1번째 주사위의 모든 숫자가 각기 바닥이 되는 경우
for c in range(6):
    # 초기화
    # 주사위 밑면 숫자
    bottom_num = arr[0][c]
    # 현재 case의 max
    current_max = 0

    for i in range(0, N):
        # 아래, 위 숫자 구하기
        bottom_index = arr[i].index(bottom_num)
        top_index = back[bottom_index]
        top_num = arr[i][top_index]

        # 옆면 숫자만 남기기
        dice_side = arr[i][:]
        dice_side.remove(bottom_num)
        dice_side.remove(top_num)

        # 옆면 중 max 구하기
        max_num = max(dice_side)
        # print(max_num)
        current_max += max_num

        # 다음 주사위 준비
        # 다음 주사위의 아랫면 숫자는 현재 주사위의 윗면.
        bottom_num = top_num
    max_case = max(max_case, current_max)

print(max_case)
