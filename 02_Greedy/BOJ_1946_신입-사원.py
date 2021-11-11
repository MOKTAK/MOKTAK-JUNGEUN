'''idea
https://www.acmicpc.net/problem/1946

시작 21.11.10 12:32
종료 21.11.10 12:

실버1


다른 모든 지원자와 비교했을 때 
서류심사 성적과 면접시험 성적 중 적어도 하나가 
다른 지원자보다 떨어지지 않는 자만 선발

즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 
서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

[아이디어]
덩치 문제랑 비슷한 것 같기도..

1 4
2 3
3 2
4 1
5 5


1 4 o
2 5 x
3 6 x
4 2 o
5 7 x
6 1 o
7 3 x

1 4 o
2 5 x
3 2 o
4 3 x
5 1 o
6 7 x
7 6 x

정당성:
최고 면접, 최고 서류 중 다른 평가를 더 잘 본 사람을 기준으로 한다.
기준보다 면접 또는 서류 점수가 높은 것이 하나라도 있으면 최적해에 포함된다.

이 사람이 최적해에 포함되지 않는다면, 
기준보다 서류 점수가 높은데도 합격하지 않으므로 문제에 모순
안됨..

정당성2:
면접기준 정렬

한명씩 훑어가며
max면접보다 서류가 높은 사람만 통과
서류가 1위인 사람 뒤에 나오는 사람은 항상 누군가보다 면접, 서류가 모두 낮아져
최적해에서 제외된다.

만약 이 사람에 최적해에 포함된다면..
이 사람은 일단 면접은 항상 낮다. (면접순으로 정렬했으므로)
서류가 1위인 사람 뒤에 나오므로, 서류 1위보다 항상 면접을 못 봤다.
또한 서류 1위인 사람이 등장하였으므로, 서류도 서류 1위보다 낮다.
즉, 서류와 면접 모두 서류1위 에 비해 적으므로 최적해에 포함될 수 없다.

정당성3:
면접기준 정렬
한명씩 훑어가며..
이미 뽑힌 사람중 서류 최하위보다 서류가 높은 사람만 최적해에 포함
이미 뽑힌 사람은 면접을 더 잘 봤으므로, 
뽑힌 사람중 서류 최하위보다 서류가 낮으면 조건에 맞지 않음.

이미 뽑힌 사람중 서류 최하위보다 서류가 높은 사람이 최적해에 포함되지 않는다면
항상 이미 뽑힌 사람보다 면접은 못 봤으므로, 서류라도 잘 봐야 합격 가능
그런데 서류 최하위보다 서류가 높은 것은 누군가보다 점수가 높으므로 붙어야..



[검색]


'''

import sys

read = sys.stdin.readline
write = sys.stdout.write

T = int(read())

def solve():
    N = int(read())
    arr = [list(map(int, read().split())) for _ in range (N)]

    max0, max1 = None, None
    for item in arr:
        found0 = False
        found1 = False
        if item[0] == 1:
            max0 = item
            found0 = True
        if item[1] == 1:
            max1 = item
            found1 = True
        if found0 and found1:
            break
    print(max0)
    print(max1)
    target = max0 if max0[1] < max1[0] else max1
    print(target)
    count = 0
    for item in arr:
        print(f"t, i = {target}, {item}")
        if item[0] <= target[0] or item[1] <= target[1]:
            print(f"add t, i = {target}, {item}")
            count += 1

    write(str(count))

def solve2():
    N = int(read())
    arr = [list(map(int, read().split())) for _ in range (N)]

    arr.sort()
    count = 0
    target = arr[0]
    for item in arr:
        if item[1] == 1:
            count += 1
            break
        if item[1] <= target[1]:
            count += 1
            target = item
        
    write(str(count)+"\n")

for _ in range(T):
    solve2()