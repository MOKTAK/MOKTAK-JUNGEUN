'''idea
https://www.acmicpc.net/problem/7568

시작: 21.10.29 10:56

제출1: 21.10.29 11:35
제출2: 21.10.29

1. 정렬을 한다.
2. 앞에서 부터 루프 돌면서 카운트

=>오류:  문제 이해를 잘 해야 함
https://www.acmicpc.net/board/view/70792

입력:
3
3 1
2 2
1 1

출력:
1 1 2

왜 1 1 3 이 아니라 1 1 2 가 출력되어야 하나요...? 

문제 예시에 따르면 앞 등수는 누적으로 처리돼서 마지막 주자는 3등으로 되어야 하는게 아닌가요?!
마지막 주자보다 키와 몸무게가 모두 큰 사람은 2번 사람으로 한 명만 있기 때문입니다.



아이디어2:
11:50 ~ 12:23
filter 써서 덩치 큰 사람만 뽑아서 출력

5
5 4 
4 5 
3 1 
2 0 
1 1 

출력 1 1 3 4 3

'''
# import sys

# read = sys.stdin.readline

# N = int(read())

# arr = [ list(map(int, read().split())) for _ in range(N)]
# # 인덱스 2: 원래 순서 삽입
# for i in range(N):
#     arr[i].append(i+1)

# # 덩치가 큰 순서대로 정렬
# arr.sort(reverse=True)

# # 비교의 기준
# before = arr[0]

# rank = 1
# # 등수 기록
# before.append(rank)

# # 같은 등수 인원
# count = 1

# for idx, item in enumerate(arr):
#     if idx == 0:
#         continue

#     # 이전 것이 덩치가 크면
#     if before[0] > item[0] and before[1] > item[1]:
#         # 누적된 인원만큼 등수에 더해주기
#         rank += count
#         item.append(rank)
#         count = 1
        
#     else:
#         item.append(rank)
#         # 같은 등수의 인원 수 추가
#         count += 1

#     # 새로운 기준
#     before = item

# # 기존 순서 기준으로 정렬
# for i in sorted(arr, key=lambda x: x[2]):
#     print(f"{i[3]}", end=" ")


import sys

read = sys.stdin.readline

N = int(read())

arr = [ list(map(int, read().split())) for _ in range(N)]

for item in arr:
    # 덩치 큰 사람 수 필터하고 출력
    print(f"{len(list(filter(lambda x: x[0] > item[0] and x[1] > item[1], arr)))+1}", end=" ")

