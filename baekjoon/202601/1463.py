"""
Docstring for ps.baekjoon.202601.1463
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1 
2
예제 출력 1 
1

예제 입력 2 
10
예제 출력 2 
3

10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.
"""
        # 0  1  2  3  4  5  6  7  8
        # 
minarr = [0, 0, 1, 1, 2]


for index in range(5, 1000001):
    tmpList = []
    if index %2 == 0:
        tmpList.append(minarr[index//2]+ 1)
    if index %3 == 0:
        tmpList.append(minarr[index//3]+ 1)
    tmpList.append(minarr[index - 1] + 1)
    minarr.append(min(tmpList))


inputNum = int(input())
print(minarr[inputNum])

# for num in range(5, 1000001):
#     print(minarr[num])