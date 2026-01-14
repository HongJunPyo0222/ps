"""
Docstring for ps.baekjoon.202601.11399
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

예제 입력 1 
5
3 1 4 3 2
예제 출력 1 
32
"""

n = int(input())
time_to_withdraw = list(map(int, input().split()))
current_time = 0

time_to_withdraw.sort()
time_waited = []



for element in time_to_withdraw:
    while element > 0:
        element -= 1
        current_time +=1
    
    time_waited.append(current_time)



print(sum(time_waited))