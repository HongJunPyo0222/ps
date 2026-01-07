"""
농부 상근이는 마당에 심기 위한 나무 묘목 n개를 구입했다. 묘목 하나를 심는데 걸리는 시간은 1일이고, 상근이는 각 묘목이 다 자라는데 
며칠이 걸리는지 정확하게 알고 있다.

상근이는 마을 이장님을 초대해 자신이 심은 나무를 자랑하려고 한다. 이장님을 실망시키면 안되기 때문에, 모든 나무가 완전히 자란 이후에 
이장님을 초대하려고 한다. 즉, 마지막 나무가 다 자란 다음날 이장님을 초대할 것이다.

상근이는 나무를 심는 순서를 신중하게 골라 이장님을 최대한 빨리 초대하려고 한다. 이장님을 며칠에 초대할 수 있을까?

입력
입력은 두 줄로 이루어져 있다. 첫째 줄에는 묘목의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄에는 각 나무가 다 자라는데 며칠이
 걸리는지를 나타낸 ti가 주어진다. (1 ≤ ti ≤ 1,000,000)

출력
첫째 줄에 며칠에 이장님을 초대할 수 있는지 출력한다. 답이 여러 가지인 경우에는 가장 작은 값을 출력한다. 묘목을 구입한 날이 1일이다.

예제 입력 1 
4
2 3 4 3

예제 출력 1 
7


예제 입력 2 
6
39 38 9 35 39 20
예제 출력 2 
42
"""

# n = int(input())
# day_remain = list(map(int, input().split()))
# day_remain.sort(reverse=True)
# current_day = 1
# #print(day_remain)

# planted_tree = []

# for current_day in range(1, len(day_remain)+ 1):
#     for index in range(current_day- 1):
#         planted_tree[index] = planted_tree[index] - 1

#     planted_tree.append(day_remain[current_day - 1])
#     #print("day", current_day, ", planted_tree: ", planted_tree)

# for _ in range(max(planted_tree)):
#     for index in range(len(planted_tree)):
#         planted_tree[index] = planted_tree[index] - 1
#     current_day +=1

# print(current_day+1)


import sys

# 입력 속도 향상을 위해 사용
input = sys.stdin.readline

n = int(input())
day_remain = list(map(int, input().split()))

# 1. 오래 걸리는 나무부터 심어야 하므로 내림차순 정렬
day_remain.sort(reverse=True)

# 2. 각 나무가 다 자라는 날짜 계산
# 나무가 다 자라는 날 = (심는 날짜) + (자라는 데 걸리는 시간)
# 심는 날짜는 1일부터 시작하므로 인덱스(i) + 1
max_day = 0
for i in range(n):
    finish_day = (i + 1) + day_remain[i]
    if finish_day > max_day:
        max_day = finish_day

# 3. 이장님은 마지막 나무가 다 자란 '다음날' 초대
print(max_day + 1)