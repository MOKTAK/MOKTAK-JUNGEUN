'''
https://www.acmicpc.net/problem/2878

시작 21.11.11 01:37

'''

'''
아이디어1
1인당 가질 사탕의 개수를 고르게 분산해준다.
오류: 더 적게 사탕을 원했던 사람이 있을 수 있다.

부족한 개수: 원하는 사탕 수 - 사탕 개수
부족한 개수 // 인원수 

각 인원이 몫 개수만큼 가짐
나머지 명은 몫+1의 개수의 사탕을 가짐

https://velog.io/@nmrhtn7898/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%88%98%ED%95%99
두 수를 더한 후, M으로 나머지 연산을 수행하는 것은 두 수를 M으로 나머지 연산을 수행한 값을 더한 후, M으로 나머지 연산을 수행하는 것과 같다.
'''
# import sys
# import collections

# read = sys.stdin.readline
# write= sys.stdout.write

# M, N = map(int, read().split())
# arr = [int(read()) for _ in range (N)]

# div = 2**64
# sum = sum(arr)
# lack = sum - M

# q, r = divmod(lack, N)
# # 인원수, 사탕수
# candy1 = [r, q+1]
# candy2 = [N-r, q]
# print(candy1)
# print(candy2)
# # (((q+1)**2 * r) + (q**2 * (N-r)))% div
# # (((q+1)**2 * r)%div +  (q**2 * (N-r))%div)%div
# result = ((((q+1)**2)%div * r%div)%div +  ((q**2)%div * (N-r)%div)%div)%div
# print(result)


"""
아이디어2: 
1. 사탕을 가장 원하는 애한테 먼저 사탕을 준다.
2. 사탕이 떨어질 때까지 1 반복

오류: 시간초과
"""
# import heapq
# import sys
# # import collections
# from collections import Counter

# read = sys.stdin.readline
# write= sys.stdout.write

# M, N = map(int, read().split())
# # 최대힙
# arr = [-int(read()) for _ in range (N)]

# div = 2**64

# heapq.heapify(arr)

# while (M > 0):
#     max = heapq.heappop(arr)
#     max += 1
#     heapq.heappush(arr, max)
#     M -= 1
# a = Counter(arr)
# count = a.most_common()
# result = 0
# for candy, num in count:
#     result += ((((candy)**2)%div * num%div)%div)
# print(result)


"""
정답
https://expresshighway.tistory.com/49
"""
import sys
candy = 0
M, N = map(int, sys.stdin.readline().strip().split())
friend = sorted([int(sys.stdin.readline()) for _ in range(N)])

rest = sum(friend) - M  # 나눠주지 못하는 사탕의 개수

answer = 0
for i in range(N):
  # 친구가 부족해하는 사탕 개수
  # 부족한 사탕 수 // 사탕을 아직 못 받은 친구 수  
  num = min(friend[i], rest // (N-i))  # 예외적인 상황을 고려한 코드
  answer += num * num
  rest -= num

print(answer % (pow(2, 64)))
