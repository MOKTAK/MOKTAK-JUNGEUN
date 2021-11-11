'''idea
https://www.acmicpc.net/problem/11047

시작 21.11.10 12:07
종료 21.11.10 12:28

실버2

[아이디어]
가장 큰 동전부터

[검색]
bisect.bisect_right(arr, x)
정렬된 arr에서 x는 몇 번째 인덱스로 들어갈지 리턴
arr에 x와 같은 값이 있다면 그 값의 오른쪽에 들어가게 리턴됨

'''
import sys
import bisect

read = sys.stdin.readline
print= sys.stdout.write

N, K= map(int, read().split())
arr = [int(read()) for _ in range (N)]

# idx: arr에 K가 들어갈 위치 
# arr에 이미 K가 있다면 오른쪽에 들어감
idx = bisect.bisect_right(arr, K)
count = 0

while K > 0:
    # ~~ 동전을 하나씩 빼는 방안: 시간초과
    # count += 1
    # K -= arr[idx-1]
    # 다음 최대 동전 구하기
    # if K < arr[idx-1]:
    #     idx =  bisect.bisect_right(arr[0:idx], K)

    # ~~ 동전을 계산해서 한 번에 빼는 방안
    # 해당 동전으로 빼야 하는 값을 한 번에 뺀다
    count += K // arr[idx-1]
    K %= arr[idx-1]
    idx =  bisect.bisect_right(arr[0:idx], K)
    
print(str(count))